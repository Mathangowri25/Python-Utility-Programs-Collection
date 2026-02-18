from list_utils3 import shallow_copy,deep_copy,nested_list

def main():
    num = []
    for _ in range(6):
        num.append(int(input("Enter the value : ")))
    a = int(input("Enter the number : "))

    shallow_copy(num)
    deep_copy(num)
    nested_list(num,a)

if __name__ == "__main__":
    main()