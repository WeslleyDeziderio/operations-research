from branch_and_bound import *

model = create_model()
nodes = [model]

dual_limit = np.inf
primal_limit = -np.inf

model, primal = branch_and_bound(nodes, model, dual_limit, primal_limit)

print("Z =", model.objective_value)
print("Solution:")
for v in model.vars:
    print(f"{v.name} = {v.x:.2f}")