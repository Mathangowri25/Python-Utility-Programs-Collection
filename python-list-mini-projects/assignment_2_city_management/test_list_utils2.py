from list_utils2 import remove_duplicate,sort_cities,Uppercase

def main():
    city = []
    for i in range(6):
        city.append(input("Enter the city : "))
    print(remove_duplicate(city))
    print(sort_cities(city))
    print(Uppercase(city))

if __name__ == "__main__":
    main()
