import sys

def read_instance(instance_path):
    try:     
        with open(instance_path) as file:
            num_vars, num_constraints = map(int, file.readline().split())
            z = [float(c) for c in file.readline().split()]

            constraints = []
            for _ in range(num_constraints):
                line = file.readline()
                constraints.append([float(c) for c in line.split()])

            print("max", z)
            print("s.a:", constraints)
            print("")

            return (num_vars, num_constraints, z, constraints)
                    
    except FileNotFoundError:
        print(f"Error: File '{instance_path}' not found.")
    except (ValueError, IndexError):
        print(f"Error: Invalid instance file format in '{instance_path}'.")

    return None