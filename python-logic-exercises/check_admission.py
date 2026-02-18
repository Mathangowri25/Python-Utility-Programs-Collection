def check_admission(marks, age, city):
    if type(marks) != int:
        raise TypeError("Corrent enter your mark")
    if type(age) != int:
        raise TypeError("Valid age to enter")
    if type(city) != str:
        raise TypeError("Valid Word to enter on city")
    
    if marks >= 70:
        if age >= 18:
            if city == "Mumbai" or city == "Pune" or city == "Delhi":
                return "Admission Approval"
    
    return "Admission Denied"

mark = int(input("Enter the obtained mark : "))
ages = int(input("Enter the your current age : "))
city = input("Enter current location : ")
print(check_admission(mark,ages,city))