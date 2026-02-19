def add_employee(directory: dict, emp_id: str, data: dict):
    if emp_id in directory:
        print(f"Employee {emp_id} already exists.")
    else:
        directory[emp_id] = data


def get_employee(directory: dict, emp_id: str):
    return directory.get(emp_id, {})


def delete_employee(directory: dict, emp_id: str):
    if emp_id in directory:
        del directory[emp_id]
    else:
        print(f"Employee {emp_id} not found.")
