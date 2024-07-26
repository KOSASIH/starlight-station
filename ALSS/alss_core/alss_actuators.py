import numpy as np

class ALSSActuators:
    def __init__(self, config):
        self.config = config
        self.actuator_type = config['actuator']['type']
        self.actuator_params = config['actuator']['params']

    def apply_action(self, action):
        if self.actuator_type == 'ideal':
            applied_action = self.ideal_actuator(action)
        elif self.actuator_type == 'nonlinear':
            applied_action = self.nonlinear_actuator(action)
        else:
            raise ValueError('Invalid actuator type')
        return applied_action

    def ideal_actuator(self, action):
        # Ideal actuator application
        applied_action = action
        return applied_action

    def nonlinear_actuator(self, action):
        # Nonlinear actuator application
        saturation_limit = self.actuator_params['saturation_limit']
        deadband_limit = self.actuator_params['deadband_limit']
        if action > saturation_limit:
            applied_action = saturation_limit
        elif action < -saturation_limit:
            applied_action = -saturation_limit
        elif abs(action) < deadband_limit:
            applied_action = 0
        else:
            applied_action = action
        return applied_action

    def get_actuator_limits(self):
        # Get the actuator limits
        return self.actuator_params['saturation_limit'], self.actuator_params['deadband_limit']

    def set_actuator_limits(self, saturation_limit, deadband_limit):
        # Set the actuator limits
        self.actuator_params['saturation_limit'] = saturation_limit
        self.actuator_params['deadband_limit'] = deadband_limit

    def save_actuator(self, filename):
        # Save the actuator to a file
        np.save(filename, self.actuator_params)

    def load_actuator(self, filename):
        # Load the actuator from a file
        self.actuator_params = np.load(filename)

    def plot_actuator_response(self, actions):
        # Plot the actuator response
        applied_actions = []
        for action in actions:
            applied_action = self.apply_action(action)
            applied_actions.append(applied_action)
        plt.plot(actions, applied_actions)
        plt.xlabel('Action')
        plt.ylabel('Applied Action')
        plt.title('Actuator Response')
        plt.show()
