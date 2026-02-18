def withdraw(balance, amount):
    if type(balance) != int:
        raise TypeError("Invalid because of Integer only support")
    if type(amount) != int:
        raise TypeError("Invalid because of Integer only support")
    
    amount = amount * 100
    if amount > balance:
        raise ValueError("Withdrawal amount exceeds balance.")
    return balance - amount


num = int(input("Enter the balance : "))
num1 = int(input("Enter the value amount :"))
print(withdraw(num,num1))