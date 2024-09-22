import numpy as np
import time

# Simulate sensor data collection for histamine and serotonin levels
def get_sensor_data():
    # Simulating histamine and serotonin levels
    # Replace these with actual sensor readings in a real implementation
    sensor_data = {
        'histamine': np.random.normal(50, 10),  # Example normal histamine level ~ 20-80 ng/mL
        'serotonin': np.random.normal(150, 30)  # Example normal serotonin level ~ 100-200 ng/mL
    }
    return sensor_data

# Function to detect inflammation based on sensor data
def detect_inflammation(sensor_data):
    # Define threshold values for histamine and serotonin
    histamine_threshold = 60  # ng/mL (example threshold for high histamine)
    serotonin_threshold = 180  # ng/mL (example threshold for high serotonin)

    histamine_level = sensor_data['histamine']
    serotonin_level = sensor_data['serotonin']
    
    # Determine inflammation status
    inflammation_status = (histamine_level > histamine_threshold or serotonin_level > serotonin_threshold)
    
    return inflammation_status

# Function to simulate real-time monitoring of inflammation
def monitor_inflammation():
    try:
        while True:
            sensor_data = get_sensor_data()  # Simulate data retrieval
            inflammation_status = detect_inflammation(sensor_data)
            
            # Print sensor data and inflammation status
            print(f"Sensor Data: {sensor_data}")
            print(f"Inflammation Detected: {'Yes' if inflammation_status else 'No'}")
            print("-" * 50)
            time.sleep(5)  # Delay for 5 seconds between readings (adjustable)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Start monitoring inflammation based on simulated sensor data
monitor_inflammation()