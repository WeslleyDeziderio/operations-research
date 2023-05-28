from utils.read_file import *
from utils.create_model import *

import numpy as np
import copy

BRANCHING_RULE = 0.5

is_integer = lambda x: x % 2 == 0
distance_to_node = lambda x: abs(x-BRANCHING_RULE)
model = create_model()

def solve_model(model):
    _ = model.optimize()

    return model

def main(nodes, model, dual_limit, primal_limit):
    dual_limit = np.inf
    primal_limit = np.inf
    leafs = [] 

    for i, node_item in enumerate(nodes):
        node: Model = node_item.copy()

        try:
            solve_model(node)
            dual_limit = min(dual_limit, node.objective_value)
        except:
            continue

if __name__ == "__main__":
    main()