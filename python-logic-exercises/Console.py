def Student_detail(name,age,mark,city):
    if type(name) != str:
        raise TypeError("Corrent value to enter")
    if type(age) != int:
        raise TypeError("Corrent value to enter")
    if type(mark) != int:
        raise TypeError("Corrent value to enter")
    if type(city) != str:
        raise TypeError("Corrent value to enter")
    
    n = name
    print(id(n))
    ag = age
    print(id(ag))
    m = mark
    print(id(m))
    c = city
    print(id(c))
    return f"Student Registered: {n}, Age: {ag}, Mark: {m}, City: {c}"

from classification_age import age_classification
from stipend_bonus import calculate_stipend_bonus
from withdraw_simulator import withdraw 
from Reverse_number import reverse_number 
from Sum_digit import sum_of_digits 
from check_admission import check_admission 
import vinod_utils 
import platform 

def Main(): 
    while True: 
        print("\nMenu:") 
        print(" 1. Register Student ") 
        print(" 2. Age Categorization ") 
        print(" 3. Stipend Bonus Calculation ") 
        print(" 4. ATM Withdrawal ") 
        print(" 5. Reverse Roll Number ") 
        print(" 6. Digit Reduction Tool ") 
        print(" 7. Admission Evaluation ") 
        print(" 8. Module Inspector ") 
        print(" 9. System Diagnostics ") 
        print(" 10. Exit ")

        choice = int(input("Enter the choice : "))
        if choice == 1:
            nam = input("Enter your name : ")
            ge = int(input("Enter the age : "))
            ma = int(input("Enter the mark : "))
            ci = input("Enter the city : ")
            print(Student_detail(nam,ge,ma,ci))
        elif choice == 2: 
            age_classification() 
        elif choice == 3: 
            calculate_stipend_bonus() 
        elif choice == 4: 
            withdraw() 
        elif choice == 5: 
            reverse_number() 
        elif choice == 6: 
            sum_of_digits() 
        elif choice == 7: 
            check_admission() 
        elif choice == 8: 
            vinod_utils.module_inspector() 
        elif choice == 9: 
            print("System:", platform.system()) 
            print("Release:", platform.release()) 
            print("Version:", platform.version()) 
        elif choice == 10: 
            print("Exiting ................") 
            break 
        else: 
            print("Invalid choice. Please select between 1 and 10.") 
            
if __name__ == "__main__": 
    Main()