
from utils.create_model import *
from collections import deque

import numpy as np

BRANCHING_RULE = 0.5
is_integer = lambda x: x == 0 or x == 1

def nearest_index(lst, K):
    return lst.index(min(lst, key = lambda x: abs(x - K)))

def solve_model(model):
    model.verbose = 0
    _ = model.optimize()

def branch_and_bound(nodes, model, dual_limit, primal_limit):
    queue = deque(nodes)
 
    while queue:
        node = queue.popleft()
        try:
            solve_model(node)
            dual_limit = min(dual_limit, node.objective_value)
        except:
            continue

        var_values = [v.x for v in node.vars]
        continuous_vars = [v.x for v in node.vars if not is_integer(v.x) and not is_integer(v.x)]

        if not continuous_vars:
            if node.objective_value > primal_limit:
                primal_limit = node.objective_value
                model = node
            continue
        
        index = nearest_index(var_values, BRANCHING_RULE)
        left_node = node.copy()
        left_node += left_node.vars[index] == 0
        queue.append(left_node)

        right_node = node.copy()
        right_node += right_node.vars[index] == 1
        queue.append(right_node)

    return model, primal_limit
    