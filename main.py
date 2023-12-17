import matplotlib
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def fitness_function(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]

    """ Apply constraints """
    penalty = 0
    obj_func_res = 16*x1 + 22*x2 + 12*x3 + 8*x4
    constraint_calc_res = 5*x1 + 7*x2 + 4*x3 + 3*x4
    if constraint_calc_res > 14:
        penalty = np.inf

    return -1 * obj_func_res + penalty

algorithm_params = {
    "max_num_iteration": None,
    "population_size": 1000,
    "mutation_probability": 0.05,
    "elit_ratio": 0.01,
    "crossover_probability": 0.5,
    "parents_portion": 0.3,
    "crossover_type": 'uniform',
    "max_iteration_without_improv": None,

}

""" Create instance of GA solver """
model = ga(function=fitness_function, dimension=4, variable_type='bool', algorithm_parameters=algorithm_params)

model.run()