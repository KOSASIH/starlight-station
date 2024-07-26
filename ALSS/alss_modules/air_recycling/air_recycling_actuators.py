**`air_recycling_sensors.py`**
```python
import time
import random
import numpy as np

class OxygenSensor:
    def __init__(self, noise_level=0.1, calibration_factor=1.0):
        self.noise_level = noise_level
        self.calibration_factor = calibration_factor

    def read_oxygen_level(self):
        # Simulate reading oxygen level with noise and calibration
        oxygen_level = 20.0 + random.uniform(-self.noise_level, self.noise_level)
        oxygen_level *= self.calibration_factor
        return oxygen_level

    def calibrate(self, calibration_factor):
        self.calibration_factor = calibration_factor

class CarbonDioxideSensor:
    def __init__(self, noise_level=0.1, calibration_factor=1.0):
        self.noise_level = noise_level
        self.calibration_factor = calibration_factor

    def read_carbon_dioxide_level(self):
        # Simulate reading carbon dioxide level with noise and calibration
        carbon_dioxide_level = 400.0 + random.uniform(-self.noise_level, self.noise_level)
        carbon_dioxide_level *= self.calibration_factor
        return carbon_dioxide_level

    def calibrate(self, calibration_factor):
        self.calibration_factor = calibration_factor

class NitrogenSensor:
    def __init__(self, noise_level=0.1, calibration_factor=1.0):
        self.noise_level = noise_level
        self.calibration_factor = calibration_factor

    def read_nitrogen_level(self):
        # Simulate reading nitrogen level with noise and calibration
        nitrogen_level = 78.0 + random.uniform(-self.noise_level, self.noise_level)
        nitrogen_level *= self.calibration_factor
        return nitrogen_level

    def calibrate(self, calibration_factor):
        self.calibration_factor = calibration_factor

class AirRecyclingSensors:
    def __init__(self):
        self.oxygen_sensor = OxygenSensor()
        self.carbon_dioxide_sensor = CarbonDioxideSensor()
        self.nitrogen_sensor = NitrogenSensor()

    def read_sensors(self):
        oxygen_level = self.oxygen_sensor.read_oxygen_level()
        carbon_dioxide_level = self.carbon_dioxide_sensor.read_carbon_dioxide_level()
        nitrogen_level = self.nitrogen_sensor.read_nitrogen_level()
        return [oxygen_level, carbon_dioxide_level, nitrogen_level]

    def calibrate_sensors(self, oxygen_calibration, carbon_dioxide_calibration, nitrogen_calibration):
        self.oxygen_sensor.calibrate(oxygen_calibration)
        self.carbon_dioxide_sensor.calibrate(carbon_dioxide_calibration)
        self.nitrogen_sensor.calibrate(nitrogen_calibration)

    def get_sensor_data(self, num_samples=100):
        sensor_data = np.zeros((num_samples, 3))
        for i in range(num_samples):
            sensor_data[i] = self.read_sensors()
            time.sleep(0.1)  # Simulate sampling rate
        return sensor_data
