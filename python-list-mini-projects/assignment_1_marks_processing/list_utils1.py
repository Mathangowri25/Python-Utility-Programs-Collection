def top_mark(mark,n):
    """
        Returns a new list containing the top n highest marks.
        The original marks list must not be modified.
    """
    if type(mark) != list:
        raise TypeError("Change the valide Datatype")
    if type(n) != int:
        raise TypeError("Change the format of correct datatype")
    sort = sorted(mark,reverse=True)
    return sort[:n]

def count_occurance(mark,value):
    """
        Returns how many times a given mark appears in the list.
    """
    if type(mark) != list:
        raise TypeError("Change the valide Datatype")
   
    val = mark.count(value)
    return val

def higher_score(mark,thro):
    """
        Returns a new list containing marks greater than or equal to threshold.
        Use list comprehension.
    """
    if type(mark) != list:
        raise TypeError("Change the valide Datatype")
    if type(thro) != int:
        raise TypeError("Change the format of correct datatype")
    
    return [i for i in mark if i>=thro]