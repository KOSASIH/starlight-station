# zero_gravity_experience_v2.py
import numpy as np
from sidra_chain_space_exploration.starlight_station.zero_gravity_experience.utils.physics_utils import PhysicsUtils
from sidra_chain_space_exploration.starlight_station.zero_gravity_experience.utils.data_processing_utils import DataProcessingUtils

class ZeroGravityExperienceModuleV2:
    def __init__(self):
        self.physics_utils = PhysicsUtils()
        self.data_processing_utils = DataProcessingUtils()

    def simulate_zero_gravity(self, astronaut_data: dict, spacecraft_data: dict, sensor_data: dict) -> dict:
        # Simulate zero gravity experience for astronaut using sensor data
        if not astronaut_data or not spacecraft_data or not sensor_data:
            raise Exception("No astronaut, spacecraft, or sensor data available")

        # Extract relevant data from astronaut, spacecraft, and sensor data
        astronaut_mass = astronaut_data["mass"]
        spacecraft_acceleration = spacecraft_data["acceleration"]
        sensor_readings = sensor_data["readings"]

        # Preprocess sensor data
        preprocessed_sensor_data = self.data_processing_utils.preprocess_sensor_data(sensor_readings)

        # Calculate the gravitational force experienced by the astronaut
        gravitational_force = self.physics_utils.calculate_gravitational_force(astronaut_mass, spacecraft_acceleration)

        # Simulate the zero gravity experience using sensor data
        zero_gravity_experience = self.physics_utils.simulate_zero_gravity(gravitational_force, preprocessed_sensor_data)

        return zero_gravity_experience

# Example usage:
zero_gravity_experience_module_v2 = ZeroGravityExperienceModuleV2()

astronaut_data = {
    "mass": 70.0,
    "height": 1.75
}

spacecraft_data = {
    "acceleration": 0.0,
    "velocity": 0.0
}

sensor_data = {
    "readings": [1.0, 2.0, 3.0, 4.0, 5.0]
}

zero_gravity_experience = zero_gravity_experience_module_v2.simulate_zero_gravity(astronaut_data, spacecraft_data, sensor_data)
print("Zero Gravity Experience:", zero_gravity_experience)
