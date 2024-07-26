import random

class WaterRecyclingSensors:
    def __init__(self):
        self.noise_level = 0.1

    def read_pH(self):
        return 7.0 + random.uniform(-self.noise_level, self.noise_level)

    def read_turbidity(self):
        return 10.0 + random.uniform(-self.noise_level, self.noise_level)

    def read_conductivity(self):
        return 100.0 + random.uniform(-self.noise_level, self.noise_level)

    def read_flow_rate(self):
        return 50.0 + random.uniform(-self.noise_level, self.noise_level)

    def read_pressure(self):
        return 10.0 + random.uniform(-self.noise_level, self.noise_level)

    def calibrate(self, calibration_factors):
        self.noise_level *= calibration_factors[0]
        self.noise_level += calibration_factors[1]
