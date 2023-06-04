
from utils.create_model import *
from copy import deepcopy
from collections import deque

import numpy as np

BRANCHING_RULE = 0.5
distance_to_node = lambda x: abs(x-BRANCHING_RULE)
is_integer = lambda x: x == 0 or x == 1

def solve_model(model):
    _ = model.optimize()
    model.verbose = 0

def branchAndBound(nodes, model, dual_limit, primal_limit):
    queue = deque(nodes)
 
    while len(queue) != 0:
        _  = queue.popleft()
        node = model.copy()
        try:
            solve_model(node)
            dual_limit = min(dual_limit, node.objective_value)
        except:
            continue

        values_relax = [v.x for v in node.vars]
        is_x_integer = [v.x for v in node.vars if not is_integer(v.x)]

        if len(is_x_integer) == 0:
            if node.objective_value > primal_limit:
                primal_limit = node.objective_value
                model = node
            continue
        
        index = distance_to_node(values_relax, BRANCHING_RULE)
        queue = [node.copy() + (node.vars[index] == 0) for node in nodes]
        queue = [node.copy() + (node.vars[index] == 1) for node in nodes]

    return model, primal_limit
    