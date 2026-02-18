def safe_integer_input(prompt):
    val = int(prompt)
    if type(val) != int:
        raise ValueError("Value must be Integer format")
    
    return "Valid Integer"

num = input("Enter any Number : ")
print(safe_integer_input(num))