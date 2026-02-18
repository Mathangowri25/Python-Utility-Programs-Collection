import copy

def shallow_copy(data:list):
    """
        Modify a nested object in the shallow copy can affect the original list
    """
    print(data)
    val = copy.copy(data)
    val[1] = 9
    print(val)

def deep_copy(data:list):
    """
        Modify a nested item in the deep-copied list cannot affect the original list
    """
    print(data)
    val = copy.deepcopy(data)
    val[2] = 5
    print(val)

def nested_list(data,value):
    """
        Appends a value to the first nested list found inside the list.
    """
    for item in data:
        if type(item) == list:
            item.append(value)
            break