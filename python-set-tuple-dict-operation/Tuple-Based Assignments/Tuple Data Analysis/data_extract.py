from data_function import get_highest_revenue,get_lowest_revenue,count_revenue_occurrence

def main():
    reven = (120000, 150000, 90000, 200000, 175000, 150000)
    val = int(input("Enter the value : "))
    print(get_highest_revenue(reven))
    print(get_lowest_revenue(reven))
    print(count_revenue_occurrence(reven,val))

if __name__ == "__main__":
    main()