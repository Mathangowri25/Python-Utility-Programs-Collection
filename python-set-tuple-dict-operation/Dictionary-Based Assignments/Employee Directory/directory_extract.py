from directory_function import add_employee,get_employee,delete_employee

def main():
    add_employee(employees, "EMP103", {"name": "Sara", "city": "Chennai", "salary": 70000})
    print(get_employee(employees, "EMP102"))
    print(get_employee(employees, "EMP999"))
    delete_employee(employees, "EMP102")
    delete_employee(employees, "EMP999")  

if __name__ == "__main__":
    main()
