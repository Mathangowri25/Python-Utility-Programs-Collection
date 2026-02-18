def sales_above(sale:list,threshold):
    """
        To categorize the sale above the threshold to print
    """
    num = []
    for i in sale:
        if i > threshold:
            num.append(i)
    return num

def sales_summary(sale:list,first:int,last:int):
    """
        To print the first order of list and last order of list
    """
    num = []
    num.append(sale[:first])
    num.append(sale[last:])
    return tuple(num)

def sales_reversed(sale:list):
    """
        To reverse the list on slicing method
    """
    return sale[::-1]

def sales_copy_sort(sale:list):
    """
        To copy on another variable and sort the value in descending order
    """
    num = sale.copy()
    n = sorted(num,reverse=False)
    return n
