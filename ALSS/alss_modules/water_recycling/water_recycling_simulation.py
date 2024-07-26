import numpy as np
import pandas as pd
from scipy.integrate import odeint
from .water_recycling_sensors import WaterRecyclingSensors
from .water_recycling_actuators import WaterRecyclingActuators

class WaterRecyclingSimulation:
    def __init__(self, sensors, actuators):
        self.sensors = sensors
        self.actuators = actuators
        self.state = np.zeros(5)  # Initialize system state

    def simulate(self, t_end, dt):
        t = np.arange(0, t_end, dt)
        states = np.zeros((len(t), 5))
        for i, ti in enumerate(t):
            states[i] = self.state
            self.state = self.update_state(ti, self.state)
        return pd.DataFrame(states, columns=['pH', 'Turbidity', 'Conductivity', 'Flow Rate', 'Pressure'])

    def update_state(self, t, state):
        # Simulate the water recycling process using ODEs
        dpH_dt = self.actuators.pH_control(state[0])
        dturbidity_dt = self.actuators.turbidity_control(state[1])
        dconductivity_dt = self.actuators.conductivity_control(state[2])
        dflow_rate_dt = self.actuators.flow_rate_control(state[3])
        dpressure_dt = self.actuators.pressure_control(state[4])
        return state + np.array([dpH_dt, dturbidity_dt, dconductivity_dt, dflow_rate_dt, dpressure_dt]) * 0.1

    def get_state(self):
        return self.state
