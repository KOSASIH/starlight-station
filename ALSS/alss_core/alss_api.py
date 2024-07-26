import os
import json
import flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from alss_actuators import ALSSActuators
from alss_data_analysis import ALSSDataAnalysis

app = flask.Flask(__name__)
api = Api(app)
CORS(app)

# Load configuration from file
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize ALSSActuators and ALSSDataAnalysis instances
actuators = ALSSActuators(config)
data_analysis = ALSSDataAnalysis(pd.read_csv(config['data_file']))

# Define API endpoints

class ActuatorAPI(Resource):
    def get(self, actuator_id):
        # Get actuator configuration
        return actuators.get_actuator_config(actuator_id)

    def put(self, actuator_id):
        # Update actuator configuration
        parser = reqparse.RequestParser()
        parser.add_argument('saturation_limit', type=float)
        parser.add_argument('deadband_limit', type=float)
        args = parser.parse_args()
        actuators.set_actuator_limits(actuator_id, args['saturation_limit'], args['deadband_limit'])
        return {'message': 'Actuator configuration updated'}

class ApplyActionAPI(Resource):
    def post(self, actuator_id):
        # Apply action to actuator
        parser = reqparse.RequestParser()
        parser.add_argument('action', type=float)
        args = parser.parse_args()
        applied_action = actuators.apply_action(actuator_id, args['action'])
        return {'applied_action': applied_action}

class DataAnalysisAPI(Resource):
    def get(self):
        # Get data analysis statistics
        return data_analysis.compute_statistics()

    def post(self):
        # Perform data analysis on uploaded data
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        data = pd.read_csv(args['data'])
        data_analysis = ALSSDataAnalysis(data)
        return data_analysis.compute_statistics()

class PlotAPI(Resource):
    def get(self, plot_type):
        # Generate plot
        if plot_type == 'time_series':
            data_analysis.plot_time_series()
        elif plot_type == 'histograms':
            data_analysis.plot_histograms()
        elif plot_type == 'correlation_matrix':
            data_analysis.plot_correlation_matrix()
        else:
            return {'error': 'Invalid plot type'}
        return {'message': 'Plot generated'}

api.add_resource(ActuatorAPI, '/actuators/<int:actuator_id>')
api.add_resource(ApplyActionAPI, '/actuators/<int:actuator_id>/apply')
api.add_resource(DataAnalysisAPI, '/data_analysis')
api.add_resource(PlotAPI, '/plots/<string:plot_type>')

if __name__ == '__main__':
    app.run(debug=True)
