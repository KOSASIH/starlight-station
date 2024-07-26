import numpy as np
from air_recycling_simulation import AirRecyclingSimulation

class AirRecyclingControl:
    def __init__(self, simulation, setpoints):
        self.simulation = simulation
        self.setpoints = setpoints

    def control(self, current_state, t):
        # Compute the error between the current state and the setpoint
        error = current_state - self.setpoints

        # Compute the control action
        control_action = np.dot(self.simulation.params['control_matrix'], error)

        return control_action

    def run_control_loop(self, initial_conditions, t_span):
        # Initialize the current state
        current_state = initial_conditions

        # Run the control loop
        for t in t_span:
            control_action = self.control(current_state, t)
            current_state = self.simulation.simulate(current_state, [t, t + 1])[1]

        return current_state

    def plot_control_results(self, control_results):
        # Plot the control results
        import matplotlib.pyplot as plt

        plt.plot(control_results[:, 0], label='Oxygen')
        plt.plot(control_results[:, 1], label='Carbon Dioxide')
        plt.plot(control_results[:, 2], label='Nitrogen')
        plt.xlabel('Time')
        plt.ylabel('Concentration')
        plt.legend()
        plt.show()
