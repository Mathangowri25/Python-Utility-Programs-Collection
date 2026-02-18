def sum_of_digits(n):
    if n < 0:
        raise ValueError("Can print only Positive value")
    
    while n >= 10:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n

num = int(input("Enter any Integer : "))
print(sum_of_digits(num))