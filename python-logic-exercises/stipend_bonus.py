def calculate_stipend_bonus(stipend, rate):
    """
        Validation:
            Stipend must be positive number.
            Rating must be integer between 1–5.
        Bonus Rules:
            Rating 5 → 30%
            Rating 4 → 20%
            Rating 3 → 10%
            Rating < 3 → 0%
        Also:
            Print id() of inputs.
            Include detailed docstring describing policy.
    """
    if stipend <= 0:
        raise ValueError("Stipend must be positive number")
    if type(rate) != int:
        raise TypeError("Rating value must be postive number")
    if rate < 1 or rate > 5: 
        raise ValueError("Rating must be between 1 and 5")

    print(id(stipend))
    print(id(rate))
    if rate == 5:
        return stipend * 0.30
    elif rate == 4:
        return stipend * 0.20
    elif rate == 3:
        return stipend * 0.10
    else:
        return stipend * 0.0
    

stipend = int(input("Enter your Stipend : "))
rate = int(input("Enter the Rating : "))
bonus = calculate_stipend_bonus(stipend, rate)
print(bonus)