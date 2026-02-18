from list_utils4 import sales_summary,sales_above,sales_copy_sort,sales_reversed

def main():
    sale = []
    for _ in range(6):
        sale.append(int(input("Enter the value : ")))
    t = int(input("Enter the threshold value : "))
    f = int(input("Enter the first appear integer : "))
    l = int(input("Enter the last appear integer : "))

    print(sales_above(sale,t))
    print(sales_summary(sale,f,l))
    print(sales_reversed(sale))
    print(sales_copy_sort(sale))

if __name__ == "__main__":
    main()