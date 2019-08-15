
#Lab 4
#part 1
"""
    Descripton:
     swaps the i-th and j-th entries in a list
    Parameters:
        list - array that contains the elements where two elements will be swapped
        i - integer of the position of the element in the array that will be swapped with j
        j - integer of the posiotn of the element in the array that will be swapped with i
    Returns:
        a list that is an array with the i-th element and the j-th element swapped
"""
def Swap(list, i, j) :
    list[i], list[j] = list[j], list[i]
    return list

#part 2
"""
    Description:
        finds the index of the smallest variable in a list
    Paramaters:
        list - a list of integers that will be iterated through to find the minimum value

    Returns:
        an integer value between 0 and len(list) that represents the position in the list of the smallest value in
        the list

    Notes:
        we removed the possibilty of also returning the value of the smallest value in the list, as the ability to return two different variables at once is wrong and should never be allowed

"""
def find_min(list) :
    temp= max(list)+1
    for i in range(len(list)) :
        if temp > list[i]:
            temp= list[i]
            postion = i
    return postion
print(find_min([2,4,5,1,9,6]))

#Part 3
"""
    Description:
        calculates selection sort as seen by the psudo-code seen in lectures

    Paramaters:
        list - a list that contains a list of integers to be sorted

    Returns:
        a list that is a sorted version of the parameter list

"""
def selection_sort_as_seen_in_lectures(list) :
    for i in range(0,len(list)) :
        m=list[i]
        j=i
        for k in range(i+1,len(list)) :
            if list[k] < m :
                m=list[k]
                j=k
        if m < list[i] :
            Swap(list,i,j)
    return list
print(selection_sort_as_seen_in_lectures([5,5,3,6,1]))


#Part 4
"""
    Description:
        calculates selection sort on a list of integers

    Paramaters:
        list - a list of integers that will be sorted by selection sort

    Returns:
        a list that is a sorted version of the parameter list

"""
def selection_sort(list) :
    for n in range(len(list)) :
        minimum_list = list[n:len(list):1]
        minimum = find_min(minimum_list)
        Swap(list,minimum+n,n)
    return list

print(selection_sort([2,4,1,3,8]))
