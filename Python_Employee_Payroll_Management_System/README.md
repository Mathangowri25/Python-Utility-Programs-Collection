# Python Employee Payroll Management System

A simple, console-based Employee Payroll Management System built in Python. This project serves as a practical demonstration of core Object-Oriented Programming (OOP) concepts, including inheritance, encapsulation, operator overloading, and custom exception handling.

## 🚀 Features

* **Object-Oriented Design:** Implements foundational OOP principles using distinct, well-structured classes.
* **Encapsulation & Data Hiding:** Secures sensitive data like employee salary using private attributes (`__salary`) and property decorators.
* **Inheritance:** Models relationships between entities (e.g., `Employee` inherits from a base `Person` class).
* **Custom Exceptions:** Includes robust error handling with a custom `InvalidSalaryError` for invalid inputs.
* **Operator Overloading:** Demonstrates Python magic methods (`__add__`, `__str__`, `__eq__`) to intuitively add salaries, display employee details, and compare employee records.
* **Class & Static Methods:** Uses `@classmethod` to manage company-wide attributes and `@staticmethod` for utility validations.

## 📂 Project Structure

* `main.py`: The entry point of the application that runs tests and displays functionality.
* `employee.py`: Contains the `Person` base class and `Employee` derived class, housing the core business logic.
* `invalid_salary_error.py`: Defines the custom exception class for handling negative or zero salary inputs.

## 💻 How to Run

1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3.  Execute the main script:
    ```bash
    python main.py
    ```

## 🛠️ Technologies Used

* Python 3.x

## 📝 Example Output

```text
Employee ID: E101, Name: Arjun, City: Bangalore, Salary: ₹50000
Employee ID: E102, Name: Meera, City: Chennai, Salary: ₹60000
Updated Salary: 55000
Total Salary: 115000
Inheritance Test: Arjun Bangalore
Company Name: Vinod Technologies
Salary Error: Salary must be greater than zero
