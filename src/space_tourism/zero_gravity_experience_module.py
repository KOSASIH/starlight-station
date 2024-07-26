# zero_gravity_experience_module.py
import numpy as np
from sidra_chain_space_exploration.starlight_station.zero_gravity_experience.utils.physics_utils import PhysicsUtils

class ZeroGravityExperienceModule:
    def __init__(self):
        self.physics_utils = PhysicsUtils()

    def simulate_zero_gravity(self, astronaut_data: dict, spacecraft_data: dict) -> dict:
        # Simulate zero gravity experience for astronaut
        if not astronaut_data or not spacecraft_data:
            raise Exception("No astronaut or spacecraft data available")

        # Extract relevant data from astronaut and spacecraft data
        astronaut_mass = astronaut_data["mass"]
        spacecraft_acceleration = spacecraft_data["acceleration"]

        # Calculate the gravitational force experienced by the astronaut
        gravitational_force = self.physics_utils.calculate_gravitational_force(astronaut_mass, spacecraft_acceleration)

        # Simulate the zero gravity experience
        zero_gravity_experience = self.physics_utils.simulate_zero_gravity(gravitational_force)

        return zero_gravity_experience

# Example usage:
zero_gravity_experience_module = ZeroGravityExperienceModule()

astronaut_data = {
    "mass": 70.0,
    "height": 1.75
}

spacecraft_data = {
    "acceleration": 0.0,
    "velocity": 0.0
}

zero_gravity_experience = zero_gravity_experience_module.simulate_zero_gravity(astronaut_data, spacecraft_data)
print("Zero Gravity Experience:", zero_gravity_experience)
