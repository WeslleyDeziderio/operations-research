import sys
class Instance:
    def __init__(self, num_vars, num_constraints, objective_function, constraints):
        self.num_vars = num_vars
        self.num_constraints = num_constraints
        self.objective_function = objective_function
        self.constraints = constraints

    def print_instance(self):
        print("Instance:", sys.argv[1])
        print("Variables:", self.num_vars)
        print("Constraints:", self.num_constraints)
        print("max:", self.objective_function)
        print("S.a:")
        for constraint in self.constraints:
            print(constraint)

def read_instance(instance_path):
    try:     
        with open(instance_path) as file:
            num_vars, num_constraints = map(int, file.readline().split())
            objective_function = [float(c) for c in file.readline().split()]

            constraints = []
            for _ in range(num_constraints):
                line = file.readline()
                constraints.append([float(c) for c in line.split()])
            return Instance(num_vars, num_constraints, objective_function, constraints)
                    
    except FileNotFoundError:
        print(f"Error: File '{instance_path}' not found.")
    except (ValueError, IndexError):
        print(f"Error: Invalid instance file format in '{instance_path}'.")

    return None