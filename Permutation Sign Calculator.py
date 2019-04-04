"""
    Description:
        calculates the signum of a chosen Composition of disjoint cycles
    Parameter:
        compositon - a list of lists, represents the compositon of the  disjoint
                cycles, each list within the list is one cycle

    Returns:
        returns either 1 or -1 depending on if the permutation is even or not
"""
def signum(compositon) :
    while(checkForCycleDecompisition(compositon)) :
        odd_inversions = list()
        for inversion in compositon :
            if (len(inversion)-1) & 2 !=0 :
                odd_inversions.append(inversion)
                if len(odd_inversions)%2 == 0 :
                    print("Group is Even")
                    return 1
                else :
                    print("Group is Odd")
                    return -1


"""
    Description:
        checks whether the cycle that has been entered is Disjoint or not
    Parameter:
        compositon - a list of lists, represents the compositon of
                cycles, each list within the list is one cycle

    Returns:
        returns either true or false depending on if the cycle compositon is
        disjoint or not
"""
def checkForCycleDecompisition(compositon) :
    numbers = list()
    for cycle in compositon :
        for number in cycle :
            numbers.append(number)
    if len(numbers) != len(set(numbers)) :
        print("CYCLE COMPOSITION IS NOT DISJOINT")
        return False
    else :
        return True
