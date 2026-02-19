def create_employee(emp_id:str,name:str,city:str,salary:float):
    if type(emp_id) != str:
        raise TypeError("Correctly enter the valid datatype")
    if type(name) != str:
        raise TypeError("Correctly enter the valid datatype")
    if type(city) != str:
        raise TypeError("Correctly enter the valid datatype")
    if type(salary) != float:
        raise TypeError("Correctly enter the valid datatype")
    print((emp_id,name,city,salary))

def update_salary(employee:tuple,new_salary):
    if type(employee) != tuple:
        raise TypeError("Enter the valid datatype")

    emp_name,id = employee
    print((emp_name,new_salary))

def get_details(employee: tuple):
    if type(employee) != tuple:
        raise TypeError("Correct the valid datatype")
    for i in employee:
        print(f"Employee details :{str(i)}")