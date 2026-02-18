def is_even(num):
    if type(num) != int:
        raise TypeError("Corrent value to enter")

    if num % 2 == 0:
        return "Number is Even"
    
def square(num):
    if type(num) != int:
        raise TypeError("Corrent value to enter")
    return num * num

def cube(num):
    if type(num) != int:
        raise TypeError("Corrent value to enter")
    return num * num * num

def format_city(city):
    if type(city) != str:
        raise TypeError("Corrent location of word to enter")
    print(f"Current location {city}")

n = int(input("Enter the number : "))
name = str(input("Enter the city : "))
print(is_even(n))
print(square(n))
print(cube(n))
format_city(name)