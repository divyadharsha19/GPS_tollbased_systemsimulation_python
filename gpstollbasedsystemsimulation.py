import logging
import simpy
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import geopy.distance
import matplotlib.pyplot as plt
import folium
import random
import uuid

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Adjust matplotlib logging level to suppress debug messages
matplotlib_logger = logging.getLogger('matplotlib')
matplotlib_logger.setLevel(logging.WARNING)

# Function to create toll areas with dynamic rates
def create_toll_areas():
    toll_areas = gpd.GeoDataFrame({
        'geometry': [Point(76.8829, 11.0168).buffer(0.01), Point(76.9509, 11.0471).buffer(0.01)],
        'rate': [0.05, 0.1]
    })
    logging.info("Toll areas created with dynamic rates")
    return toll_areas

# Function to create Folium map with toll zones
def create_folium_map(toll_areas):
    # Coimbatore coordinates
    coimbatore_coords = (11.0168, 76.9558)
    
    # Create the map centered around Coimbatore
    coimbatore_map = folium.Map(location=coimbatore_coords, zoom_start=12)
    
    # Add markers for toll areas
    for idx, toll_area in toll_areas.iterrows():
        folium.Marker([toll_area.geometry.centroid.y, toll_area.geometry.centroid.x],
                      popup=f"Toll Area {idx}",
                      icon=folium.Icon(color='red')).add_to(coimbatore_map)
    
    return coimbatore_map

class Car:
    def __init__(self, simulation_env, start_point, end_point):
        self.simulation_env = simulation_env
        self.car_id = uuid.uuid4()
        self.current_location = start_point
        self.final_location = end_point
        self.path = LineString([start_point, end_point])
        self.total_distance = 0
        self.locations_visited = [start_point]
        self.total_toll_fee = 0
        self.tolls_crossed = []
        self.speed = random.uniform(40, 60)  # Speed in km/h
        self.fuel_level = 100.0  # Fuel level in percentage
        self.status = 'running'
        self.fuel_consumption_rate = random.uniform(0.05, 0.1)  # Fuel consumption rate per km

    def drive(self):
        while self.current_location != self.final_location and self.status == 'running':
            if self.fuel_level <= 0:
                self.status = 'stopped'
                logging.warning(f"Car {self.car_id} has stopped due to no fuel.")
                break

            yield self.simulation_env.timeout(1)
            self._update_location()
            self._consume_fuel()
            self.total_distance += geopy.distance.distance(self.current_location, self.final_location).km
            self.locations_visited.append(self.current_location)
            logging.debug(f"Car {self.car_id} moved to {self.current_location}")
        
        if self.status == 'stopped':
            logging.info(f"Car {self.car_id} has stopped at {self.current_location}")
        else:
            logging.info(f"Car {self.car_id} reached its final destination at {self.final_location}")

    def refuel(self, amount):
        self.fuel_level = min(self.fuel_level + amount, 100.0)
        logging.info(f"Car {self.car_id} refueled to {self.fuel_level}%.")

    def check_status(self):
        logging.info(f"Car {self.car_id} status: {self.status}, fuel level: {self.fuel_level}%.")

    def _update_location(self):
        lat_step = (self.final_location[0] - self.current_location[0]) * (self.speed / 100)
        lon_step = (self.final_location[1] - self.current_location[1]) * (self.speed / 100)
        self.current_location = (self.current_location[0] + lat_step, self.current_location[1] + lon_step)

    def _consume_fuel(self):
        self.fuel_level -= self.speed * self.fuel_consumption_rate
        if self.fuel_level <= 0:
            self.status = 'stopped'

def detect_toll_crossing(car, toll_areas):
    car_path = LineString([car.current_location, car.final_location])
    for i, toll_area in enumerate(toll_areas['geometry']):
        if car_path.intersects(toll_area):
            car.tolls_crossed.append(i)
            logging.info(f"Car {car.car_id} crossed toll area {i}")

def compute_toll_fees(car, toll_areas, current_time):
    peak_hours = [(7, 9), (17, 19)]
    base_rate = 0.05

    is_peak_time = any(start <= current_time % 24 < end for start, end in peak_hours)
    for toll_area, rate in zip(toll_areas['geometry'], toll_areas['rate']):
        fee_rate = rate * 1.5 if is_peak_time else rate
        if car.path.intersects(toll_area):
            distance_within_area = car.path.intersection(toll_area).length
            toll_fee = distance_within_area * fee_rate
            car.total_toll_fee += toll_fee
            logging.info(f"Toll fee for Car {car.car_id} at time {current_time}: {toll_fee}")

def process_payment(account, toll_fee):
    account_balances = {'account1': 100.0}
    if account_balances[account] >= toll_fee:
        account_balances[account] -= toll_fee
        logging.info(f"Toll fee of {toll_fee} deducted from {account}. Remaining balance: {account_balances[account]}")
    else:
        logging.warning(f"Insufficient balance for {account}")

def create_car_movements_graph(cars):
    # Prepare data for graph (simulated distances over time)
    time_steps = range(10)  # 10 time steps
    car_data = {f"Car {car.car_id}": [random.uniform(0, 100) for _ in time_steps] for car in cars}
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    for car, data in car_data.items():
        plt.plot(time_steps, data, marker='o', label=car)
    
    plt.xlabel('Time Steps')
    plt.ylabel('Distance (km)')
    plt.title('Simulated Car Movements')
    plt.legend()
    plt.grid(True)
    
    # Display the plot
    plt.show()

def main():
    logging.info("Starting the simulation...")
    sim_env = simpy.Environment()
    
    # Creating 5 cars for simulation with random start and end points
    cars = [Car(sim_env, (random.uniform(11.0100, 11.0200), random.uniform(76.9600, 76.9700)), 
                        (random.uniform(11.0300, 11.0400), random.uniform(76.9500, 76.9600))) for _ in range(5)]
    logging.info(f"{len(cars)} cars created for simulation.")
    
    for car in cars:
        sim_env.process(car.drive())
    
    sim_env.run(until=10)
    logging.info("Simulation completed.")
    
    current_time = 8
    logging.info(f"Current time for toll computation: {current_time}.")
    
    toll_areas = create_toll_areas()
    
    for car in cars:
        logging.info(f"\nCar ID: {car.car_id}")
        logging.info(f"Initial Location: {car.current_location}")
        logging.info(f"Final Destination: {car.final_location}")
        
        detect_toll_crossing(car, toll_areas)
        compute_toll_fees(car, toll_areas, current_time)
        process_payment('account1', car.total_toll_fee)
        car.check_status()
    
    # Create Folium map and save it as an HTML file
    folium_map = create_folium_map(toll_areas)
    folium_map.save('THE_BEST_TECHIES_MAP.html')
    
    # Create car movements graph
    create_car_movements_graph(cars)

if __name__ == "__main__":
    main()
