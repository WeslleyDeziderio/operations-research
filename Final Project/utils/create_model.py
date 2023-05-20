from mip import Model, xsum, BINARY, MAXIMIZE, CBC, OptimizationStatus
from utils.read_file import *

def create_model():
    model = Model(sense=MAXIMIZE, solver_name=CBC)
    x = [model.add_var(var_type=BINARY, name=f"x_{i}") for i in range (read_instance(sys.argv[1])[0])]