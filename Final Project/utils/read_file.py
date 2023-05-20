def read_instance(instance_path):
    try:     
        with open(instance_path) as file:
            list_ = [list(map(int, row.split())) for row in file]
            num_vars = list_[0][0]
            num_constraints = list_[0][1]
            list_.pop(0)

            coefficients = list_[0]
            list_.pop(0)

            constraints = list_

            return num_vars, num_constraints, coefficients, constraints
        
    except FileNotFoundError:
        print(f"Error: File '{instance_path}' not found.")
    except (ValueError, IndexError):
        print(f"Error: Invalid instance file format in '{instance_path}'.")

    return None