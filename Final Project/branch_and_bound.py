from utils.read_file import *
from mip import *

import sys

RELAX_RULE = 0.5

# def create_model(qtt_variables, qtt_constraints):
#     model = Model(sense=MAXIMIZE, solver_name=CBC)
#     x = [model.add_var(var_type=BINARY, name=f"x_{i}") for i in range (n)]

def main():
    print("Hello, world")
    read_instance(sys.argv[1])

main()