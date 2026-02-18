def remove_duplicate(city:list):
    """
        By removing the duplicate value from the list
    """
    if type(city) != list:
        raise TypeError("Change over the valid list")
    cities = []
    for citi in city:
        if citi not in cities:
            cities.append(citi)
    return cities

def sort_cities(city:list):
    """
        Sorting the list in Alphabetical order
    """
    if type(city) != list:
        raise TypeError("Change over the valid list")
    sorts = sorted(city,reverse = False)
    return sorts

def Uppercase(city:list):
    """
        To change over the list of word in Uppercase format
    """
    cities = []
    for i in city:
        if type(i) != str:
            raise TypeError("Must the value be in string format")
        else:
            cities.append(i.upper())
    return cities