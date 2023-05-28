from mip import Model, xsum, BINARY, MAXIMIZE, CBC, OptimizationStatus
from utils.read_file import *

def create_model():
    instance = read_instance(sys.argv[1])
    instance.print_instance()

    model = Model(sense=MAXIMIZE, solver_name=CBC)
    x = [model.add_var(var_type=BINARY, name=f"x_{i}") for i in range(instance.num_vars)]
    model.objective = xsum(instance.objective_function[i] * x[i] for i in range(instance.num_vars))

    for i in instance.constraints:
        model += xsum(i[j] * x[j] for j in range(instance.num_vars)) <= i[-1]

    model.write("model.lp")
