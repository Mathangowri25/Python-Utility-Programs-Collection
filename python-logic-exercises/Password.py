def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
     
    upper = False
    for i in password: 
        if i.isupper(): 
            upper = True 
            break 
        if not upper: 
            raise ValueError("At least one uppercase character must be present") 
    digit = False 
    for i in password: 
        if i.isdigit(): 
            digit = True 
            break 
        if not digit: 
            raise ValueError("At least one digit must be present") 
            
    print("Valid Password")

pattern = input("Enter the password to check : ")
print(validate_password(pattern))