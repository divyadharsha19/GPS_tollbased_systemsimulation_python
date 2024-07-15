---

# GPS Toll-Based System Simulation using Python

## Overview

The Python code simulates a scenario involving vehicles moving between random start and end points in a simulated city environment (modeled Coimbatore, India). The simulation incorporates GPS-based tracking of vehicle movements, dynamic toll calculation based on predefined toll areas, and interactive visualization of vehicle paths and toll zones using Folium and Matplotlib libraries.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [Simulation Details](#simulation-details)
6. [Usage](#usage)
7. [Implementation challenge](#Implementation-challenge)
8. [Contributors](#contributors)
9. [Where to Get Help](#where-to-get-help)
10. [License](#license)
11. [Planned Enhancements](#planned-enhancements)

## Features

- **Vehicle Movement Simulation**: Simulate vehicles moving along predefined GPS coordinates.
  
- **Toll Zone Definition**: Define toll zones or points with specific GPS coordinates.
  
- **Distance Calculation**: Calculate the distance traveled by each vehicle within toll zones.
  
- **Toll Calculation**: Compute toll charges based on distance traveled or zones passed.
  
- **Payment Simulation**: Simulate the deduction of toll charges from user accounts.
## Ensuring GPS-Like Functionality
- **Geographic Coordinates**:
  Uses latitude and longitude to define start points, end points, and toll areas, mimicking GPS coordinates.
- **Simulated Movement**:
  Updates car positions incrementally to simulate driving, akin to GPS tracking.
- **Distance Calculation**:
  Uses geopy.distance to measure distances between coordinates, similar to how GPS calculates distance traveled.

## Dependencies

This project depends on several Python libraries:

- **SimPy**
- **GeoPandas**
- **Pandas**
- **Geopy**
- **Matplotlib**
- **Folium**
- **UUID**
- **Random**

## Installation

To run the GPS toll-based system simulation project, follow these steps:

### Clone the repository:

```bash
git clone https://github.com//your_repository.git
cd your_repository
```
## Example
```
git clone https://github.com/divyadharsha19/GPS_simulation_python.git
cd GPS_simulation_python
```

### Install dependencies:

Ensure you have Python 3.x installed. Install required Python packages using pip:

```bash
pip install simpy geopandas pandas geopy matplotlib folium uuid random
```

### Setup environment:

It's recommended to use a virtual environment (e.g., virtualenv or conda) to manage dependencies and isolate the project environment.

```bash
# Example using virtualenv
virtualenv venv
source venv/bin/activate  # On Windows use `source venv\Scripts\activate`
```
## Prerequisites

Before running the project, ensure you have the following:

- **Python Installed**: Ensure Python (preferably Python 3) is installed on your system.

- **Required Python Packages**: Install the necessary Python packages if you haven't already. You can install them using `pip`, Python's package installer.

  ```sh
  pip install simpy geopandas pandas geopy matplotlib folium
  
### Simulation Details
## Project Structure
## The project is structured as follows:
**Main Script**:  
- filename.py - Entry point for running the simulation.
  
**Data Files**:
- Includes data files for defining start points, end points, and toll areas.

**FunctionsVisualization**:
-  Outputs include HTML maps (THE_BEST_TECHIES_MAP.html) and graphs (car_movements_graph.png) to visualize simulation results.

## Function Details
**create_toll_areas()**
- Creates predefined toll areas with dynamic rates using GeoPandas.

**create_folium_map(toll_areas)**
- Generates a Folium map centered around Coimbatore, India, with markers for toll zones.
  
**Car Class contains**
- Represents a vehicle in the simulation with methods for driving, refueling, and checking status.

**detect_toll_crossing(car, toll_areas)**
- Detects if a vehicle crosses any defined toll areas during its journey.

**compute_toll_fees(car, toll_areas, current_time)**
- Calculates toll fees for a vehicle based on its path intersections with toll areas, considering peak and off-peak hours.

**process_payment(account, toll_fee)**
- Simulates the deduction of toll fees from a user account.

**create_car_movements_graph(cars)**
- Creates a plot illustrating simulated car movements over time.

## Libraries Used
**SimPy**: 
 - For discrete-event simulation.
   
**GeoPandas**:
 - For manipulating geographic data.
   
**Pandas**:
 - For data manipulation and analysis.
   
**Geopy**:
 - For calculating distances between coordinates.
   
**Matplotlib**:
 - For plotting graphs.
   
**Folium**:
 - For creating interactive maps.
   
**UUID**:
 - For generating unique identifiers.
   
**Random**:
 - For generating random numbers.
## Usage

Follow these steps to use the GPS toll-based system simulation:

1. **Start the simulation**:

   Execute the main script to start the simulation:
   
   ```bash
   python filename.py
   ```

2. **View output**:

   The script generates visualizations (map and graphs) to illustrate vehicle movements, toll zones, and other relevant data.

3. **Interact with the map**:

   Open `THE_BEST_TECHIES_MAP.html` in a web browser to view the Folium map showing Coimbatore, India, with marked toll zones.

4. **Explore the graph**:

   Check `car_movements_graph.png` for the plot illustrating simulated car movements over time.

5. **Understand the console output**:

   Console logs provide real-time updates on car status, toll crossings, and payment details.
   
## Implementation Challenges
**Accuracy**:
  - Simulating realistic vehicle movements and accurately detecting toll zone crossings can 
be complex.

**Performance**:
  - Handling a large number of simulated vehicles and toll transactions may require 
optimization for performance. 

**Complexity**:
  - Integrating different aspects of the simulation (movement, payment, reporting) 
requires careful design to ensure the system's components work together seamlessly. 
   

## Contributors

- Divyadharshini S 
- Bhuvaneshwari S
- Janikaa S

## Where to Get Help

For any inquiries or assistance, feel free to reach out via email: divyadharshini19cse@gmail.com. This project is a mini startup with ongoing enhancements planned in future iterations, developed with the support of online resources and repositories.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Planned Enhancements
- Enhanced Vehicle Dynamics:
Introduce varying vehicle speeds based on traffic density and road conditions.
Implement realistic acceleration and deceleration models.
- Dynamic Toll Pricing:
Incorporate algorithms for real-time toll adjustments based on traffic volume and congestion.
- Multi-modal Simulation:
Extend the simulation to include public transport and bicycle movements interacting with vehicles.
- User Interaction:
Develop a user interface for configuring simulation parameters and visualizing real-time data.
- Scenario Expansion:
Include additional cities or regions to simulate diverse geographical scenarios.
