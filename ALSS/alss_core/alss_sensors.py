import numpy as np
import pandas as pd

class ALSSSensors:
    def __init__(self, config):
        self.config = config
        self.sensor_type = config['sensor']['type']
        self.sensor_params = config['sensor']['params']

    def measure(self, state):
        if self.sensor_type == 'ideal':
            measurement = self.ideal_sensor(state)
        elif self.sensor_type == 'noisy':
            measurement = self.noisy_sensor(state)
        else:
            raise ValueError('Invalid sensor type')
        return measurement

    def ideal_sensor(self, state):
        # Ideal sensor measurement
        measurement = state
        return measurement

    def noisy_sensor(self, state):
        # Noisy sensor measurement
        noise_std = self.sensor_params['noise_std']
        measurement = state + np.random.normal(0, noise_std, size=state.shape)
        return measurement

    def get_measurement_noise(self):
        # Get the measurement noise standard deviation
        return self.sensor_params['noise_std']

    def set_measurement_noise(self, noise_std):
        # Set the measurement noise standard deviation
        self.sensor_params['noise_std'] = noise_std

    def save_sensor(self, filename):
        # Save the sensor to a file
        np.save(filename, self.sensor_params)

    def load_sensor(self, filename):
        # Load the sensor from a file
        self.sensor_params = np.load(filename)

    def get_sensor_data(self, state_data):
        # Get the sensor data from the state data
        sensor_data = []
        for state in state_data:
            measurement = self.measure(state)
            sensor_data.append(measurement)
        return sensor_data

    def plot_sensor_data(self, sensor_data):
        # Plot the sensor data
        plt.plot(sensor_data)
        plt.xlabel('Time')
        plt.ylabel('Measurement')
        plt.title('Sensor Data')
        plt.show()
