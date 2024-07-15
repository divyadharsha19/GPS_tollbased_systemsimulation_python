### Architecture Overview

**Main Script (filename.py)**:
- **Entry Point**:
     - Orchestrates the entire simulation process.
- **Simulation Environment Setup**
    - Initializes SimPy environment (sim_env) for event-driven simulation.
**Data Management**:
- **GeoSpatial Data Handling**:
    -  Utilizes GeoPandas (geopandas) for managing geographic data, defining toll areas with specific rates.
- **Visualization Data**:
    - Generates visualizations using Matplotlib (matplotlib) for car movements and Folium (folium) for interactive maps.
## Simulation Components:

**Car Class**:
- **Attributes**:
    - Tracks car ID, current location, final destination, path, distances traveled, toll fees, and status.
      
**Methods**:
- **drive()**:
    - Simulates car movement towards the destination, updating location, consuming fuel, and logging movements.
- **refuel(amount)**:
    - Allows refueling to maintain travel capability.
- **check_status()**:
   -  Logs current car status and fuel level.
- **Dependencies**:
    -  Utilizes uuid for unique identifiers and random for generating random values (e.g., speed, fuel consumption).
## Toll Management:
## Functions:
- **create_toll_areas()**:
   -  Defines toll zones with dynamic rates.
- **detect_toll_crossing(car, toll_areas)**:
   - Checks if a car crosses any defined toll areas during its journey.
- **compute_toll_fees(car, toll_areas, current_time)**:
   - Calculates toll fees based on car's path intersections with toll areas, considering peak/off-peak hours.
- **process_payment(account, toll_fee)**:
   -  Simulates deduction of toll fees from user account balance.
   -  
## Visualization and Output:

## Folium Map Generation:
**create_folium_map(toll_areas)**:
- Creates an interactive map using Folium, marking toll zones in Coimbatore, India.
  
## Graphical Representation:
**create_car_movements_graph(cars)**:
- Generates a plot illustrating simulated car movements over time using Matplotlib.
  
## Logging and Debugging:
**Logging Setup**: 
- Configures logging using logging module to capture simulation events, errors, and status updates.
Debugging: Suppresses debug messages from Matplotlib to maintain clarity in console output.
