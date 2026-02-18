def reverse_number(n):
    if n < 0:
        raise ValueError("Can print only Positive value")
    rem = 0
    while(n>0):
        digit = n % 10
        rem = rem * 10 + digit
        n //= 10

    return rem

num = int(input("Enter any Integer : "))
print(reverse_number(num))