import json

class ALSSConfig:
    def __init__(self, config_file='alss_config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def get_simulation_settings(self):
        return self.config['simulation']

    def get_control_settings(self):
        return self.config['control']

    def get_sensor_settings(self):
        return self.config['sensors']

    def get_actuator_settings(self):
        return self.config['actuators']

    def get_data_analysis_settings(self):
        return self.config['data_analysis']

    def get_visualization_settings(self):
        return self.config['visualization']

    def get_api_settings(self):
        return self.config['api']
