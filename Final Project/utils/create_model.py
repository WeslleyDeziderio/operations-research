from mip import Model, xsum, BINARY, MAXIMIZE, CBC, OptimizationStatus
from utils.read_file import *

import numpy as np

def create_model():
    instance = read_instance(sys.argv[1])
    instance.print_instance()

    z_dual = np.inf
    z_primal = np.inf

    model = Model(sense=MAXIMIZE, solver_name=CBC)
    x = [model.add_var(var_type=BINARY) for _ in range(instance.num_vars)]
    model.objective = xsum(instance.objective_function[i] * x[i] for i in range(instance.num_vars))

    for i in instance.constraints:
        model += xsum(i[j] * x[j] for j in range(instance.num_vars)) <= i[-1]

    model.optimize()
    z = model.objective_value
    for v in model.vars:
        print(f"{v.name}: {v.x}")
        
    print(f"z = {z}")
