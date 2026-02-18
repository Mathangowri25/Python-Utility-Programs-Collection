def interest_growth_analyzer(principal, rate):
    if rate <= 0:
        raise ValueError("Rate must be greater than 0.")
    target = principal * 2
    amount = principal
    years = 0
    while amount < target:
        years += 1
        amount += amount * (rate / 100)
        print(f"Year {years}: {amount:.2f}")

    print(f"\nIt takes {years} years to double the amount.")

p = float(input("Enter principal amount: "))
r = float(input("Enter yearly interest rate (%): "))
interest_growth_analyzer(p, r)