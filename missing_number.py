

def find_missing(list1, list2):
    """(list, list) -> int

    Takes two arrays, all containing positive integers and compares them
    Returns the unique number or 0 if both arrays are equal or empty
    """
    set1, set2 = set(list1), set(list2)

    if set1 == set2 or len(set1) == 0 and len(set2) == 0:
        return 0
    else:
        return (set1.symmetric_difference(set2)).pop()