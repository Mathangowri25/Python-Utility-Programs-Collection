from invalid_salary_error import InvalidSalaryError

class Person:
    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city

    def get_details(self) -> str:
        return f"Name: {self.name}, City: {self.city}"

class Employee:
    company_name = "Vinod Technologies" 

    def __init__(self, emp_id: str, name: str, city: str, salary: float):
        super().__init__(name, city)

        if not Employee.is_valid_salary(salary):
            raise InvalidSalaryError("Salary must be greater than zero")

        self.emp_id = emp_id
        self.__salary = salary   

    @property
    def get_salary(self) -> float:
        return self.__salary

    @__salary.Setter
    def update_salary(self, new_salary: float) -> None:
        if not Employee.is_valid_salary(new_salary):
            raise InvalidSalaryError("Salary must be greater than zero")
        self.__salary = new_salary

    def get_details(self) -> str:
        return (
            f"Employee ID: {self.emp_id}, "
            f"Name: {self.name}, "
            f"City: {self.city}, "
            f"Salary: ₹{self.__salary}"
        )

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary > 0

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Can only add Employee objects")
        return self.__salary + other.__salary

    def __str__(self):
        return self.get_details()

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.emp_id == other.emp_id

    @classmethod
    def change_company_name(cls, new_name: str):
        cls.company_name = new_name