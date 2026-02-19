from employee_function import create_employee,update_salary,get_details

def main():
    id = input("ENter your empoyee id : ")
    name = input("Enter your employee name : ")
    city = input("Enter the currect city : ")
    salary = float(input("Enter the salary : "))
    val = (name,id)
    create_employee(id,name,city,salary)
    update_salary(val,salary)
    get_details(val)

if __name__ == "__main__":
    main()