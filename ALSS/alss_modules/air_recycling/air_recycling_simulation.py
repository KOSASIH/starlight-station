import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

class AirRecyclingSimulation:
    def __init__(self, params):
        self.params = params

    def simulate(self, initial_conditions, t_span):
        # Define the system of ODEs
        def system(y, t, params):
            # Extract variables
            oxygen = y[0]
            carbon_dioxide = y[1]
            nitrogen = y[2]

            # Compute derivatives
            doxygen_dt = params['k1'] * oxygen * carbon_dioxide - params['k2'] * oxygen * nitrogen
            dcarbon_dioxide_dt = params['k3'] * carbon_dioxide * nitrogen - params['k4'] * carbon_dioxide * oxygen
            dnitrogen_dt = params['k5'] * nitrogen * oxygen - params['k6'] * nitrogen * carbon_dioxide

            return [doxygen_dt, dcarbon_dioxide_dt, dnitrogen_dt]

        # Solve the system of ODEs
        solution = odeint(system, initial_conditions, t_span, args=(self.params,))

        return solution

    def optimize(self, initial_conditions, t_span, objective_function):
        # Define the objective function
        def objective(params):
            solution = self.simulate(initial_conditions, t_span, params)
            return objective_function(solution)

        # Minimize the objective function
        result = minimize(objective, self.params, method='SLSQP')

        return result.x

    def plot_results(self, solution):
        # Plot the results
        import matplotlib.pyplot as plt

        plt.plot(solution[:, 0], label='Oxygen')
        plt.plot(solution[:, 1], label='Carbon Dioxide')
        plt.plot(solution[:, 2], label='Nitrogen')
        plt.xlabel('Time')
        plt.ylabel('Concentration')
        plt.legend()
        plt.show()
