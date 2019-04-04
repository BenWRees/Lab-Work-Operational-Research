import numpy
"""
    Description:
         function that takes a list or numpy array and
         moves the smallest element to the start of the array.
    Parameter:
        list - a list that is unsorted
    Returns:
        returns the list with the smallest element of the list pushed to the
        front
"""

def sort_minimum(list) :
    min_value =0
    #sort through all the inices of list
    for i in range(len(list)) :
        if list[i] < min_value :
            min_value,list[i] = list[i],min_value
        else :
            min_value,list[i] = min_value,list[i]

    list[0], min_value = min_value, list[0]
    return list


"""
    Description:
        function that takes a list or numpy array and
        sorts it in ascending order using bubble sort
    Parameter:
        list - a list or tuple that is unsorted
    Returns:
        the parameter list that has been sorted in ascending order
"""
def bubble_sort(list) :
    n = len(list)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return list
"""
    Description:
        function complex_sort that given a list or numpy array of
        complex numbers sorts them in ascending order of magnitude
    Parameter:
        list - a list or tuple that is unsorted and in all elements are in the
        complex field
    Returns:
        the parameter list that has been sorted in ascending order,by order of
        each elements magnitude
"""
def complex_sort(list) :
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if abs(list[j]) > abs(list[j+1]) :
                list[j], list[j+1] = list[j+1], list[j]
    return list


print(complex_sort([-2, 1 + 1j, 2 + 1j, 5 - 1j]))
