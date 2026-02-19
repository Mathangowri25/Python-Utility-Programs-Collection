def get_highest_revenue(revenues: tuple):
    if type(revenues) != tuple:
        raise TypeError("Enter the valid datatype")
    higher = sorted(revenues,reverse=True)
    return higher[0]

def get_lowest_revenue(revenues: tuple):
    if type(revenues) != tuple:
        raise TypeError("Enter the valid datatype")
    lower = sorted(revenues,reverse=False)
    return lower[0]

def count_revenue_occurrence(revenues: tuple, value: int):
    if type(revenues) != tuple:
        raise TypeError("Enter the valid datatype")
    count = 0
    for num in revenues:
        if num == value:
            count += 1
    return count