def age_classification(num):
    if type(num) != int:
        raise TypeError("To enter the correct format of value")
    if num < 0 and num > 120:
        raise ValueError("No, Enter the correct age of the age")
    
    if num >= 0 and num <= 12 :
        return "You is Child"
    elif num >= 13 and num <= 19:
        return "You is Teenager"
    elif num >= 20 and num <= 59:
        return "You is Adult"
    else:
        return "you is Senior Citizen"
        
age = int(input("Enter your currect age :"))
print(id(age))
print(age_classification(age))