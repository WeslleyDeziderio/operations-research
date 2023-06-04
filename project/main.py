from branch_and_bound import *

model = create_model()
nodes = [model]

dual_limit = np.inf
primal_limit = -np.inf

model, primal = branchAndBound(nodes, model, dual_limit, primal_limit)

print(model.objective_value)
print("Solution:")
for v in model.vars:
    print(f"{v.name} = {v.x:.2f}")