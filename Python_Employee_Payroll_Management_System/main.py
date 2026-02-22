from employee import Employee
from invalid_salary_error import InvalidSalaryError


def main():
    try:
        emp1 = Employee("E101", "Arjun", "Bangalore", 50000)
        emp2 = Employee("E102", "Meera", "Chennai", 60000)
        print(emp1.get_details())
        print(emp2.get_details())

        emp1.update_salary(55000)
        print("Updated Salary:", emp1.get_salary())
        total_salary = emp1 + emp2
        print("Total Salary:", total_salary)
        print("Inheritance Test:", emp1.name, emp1.city)
        print("Company Name:", Employee.company_name)
        emp3 = Employee("E103", "Ravi", "Mumbai", -20000)

    except InvalidSalaryError as e:
        print("Salary Error:", e)

    except TypeError as e:
        print("Type Error:", e)


if __name__ == "__main__":
    main()