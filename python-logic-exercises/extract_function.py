from vinod_utils import is_even
from vinod_utils import square
from vinod_utils import cube
from vinod_utils import format_city

def Main():
    a = int(input("Enter the value : "))
    c = input("Enter the word : ")
    print(is_even(a))
    print(square(a))
    print(cube(a))
    print(format_city(c))

Main()