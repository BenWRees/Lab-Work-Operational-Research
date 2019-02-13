import numpy as np
import matplotlib.pyplot as plot

#Lab 1
#Part 1
"""
    Description:
        Computes the factorial of a certain number
    Parameter:
        n - an integer value that is the greatest value in the factorial series n!
    Returns:
        an integer value of n!
"""

def Factorial(n) :
    if n>0 :
        return n*Factorial(n-1)
    else :
        return 1
print(Factorial(6))

#Part 2

width = 2
height = 3
depth = 2
volume = width*height*depth
print(volume)
print("the volume has been calculated by taking the values stored in the variables of width, height and depth and multiplying them together. \n")


#Part 3
"""
    Description:
        Calculates the volume of any 3d surface by finding the product of it's width, height and depth
    Parameters:
        width - integer or float value of the value of the surfaces norm parallel to the y-axis
        height - integer or float value of the value of the surfaces norm parallel to the z-axis
        depth - integer or float value of the value of the surfaces norm parallel to the x-axis
    Returns:
        returns an integer or float value that is the volume of the surface with the dimensions inputted
"""

def Volume(width, height, depth) :
    return width*height*depth
print(Volume(3,3,3))

#Lab 2
#Part 1
"""
    Description:
        flips a string in reverse order
    Parameters:
        s - string that will be flipped into reverse order
    Returns:
        a string that is the reversed form of the parameter s
"""

def Flip(s) :
    temp=s[1:len(s):]
    temp=temp[::-1]
    s=s[0]+temp
    return s
print(Flip("abc"))

#Part 2

for n in [1.0,2.0,3.0,4.0,5.0] :
    print(1/(n**4))

#Part 3

summation = 0
for p in range(2,6) :
    for n in range(1,1000) :
        summation = n**(-p)
    print(summation)

#Lab 3
A = np.array([[1.0, 4.0, 3.0, 2.0],
                 [2.0, -7.0, 5.0, 1.0],
                 [1.0, 2.0, 6.0, 0.0],
                 [2.0, -10.0, 3.0, 4.0]])
B = np.array([[5.0, 2.0, -4.0, -2.0],
                 [-3.0, 1.0, 5.0, 1.0],
                 [4.0, -1.0, 1.0, 3.0],
                 [2.0, 1.0, -1.0, 1.0]])
C = np.array([[3.0, 0.0, 0.0, 0.0],
                 [7.0, -6.0, 0.0, 0.0],
                 [2.0, -1.0, -1.0, 0.0],
                 [-4.0, -2.0, 2.0, -2.0]])

#Lab 3
#Part 1
"""
    Description:
        Does one step of gaussian elimination in bringing a matrix to upper triangular
    Parameters:
        A - multi-dimensional Array that acts as a matrix
        r1 - integer value that represents the row that is being replaced
        r2 - integer value of row that is taking away from row being replaced
    Returns:
        Matrix that has undergone one step of gaussian elimination closer to upper triangular form
"""
def Row_Elimination(A, r1, r2) :
    e = (A[r2][r1])/(A[r1][r1])
    A[r1] = A[e*r1] - A[r2]
    return A
print(Row_Elimination(A,2,1))

#Part 2 - NEED TO FIX ALL BUT DET(C)
"""
    det((A^T)(B^-1))
"""
D1 = np.linalg.det(A)
D2 = np.linalg.det(B)
Det1 = D1/D2
print(Det1)
"""
    det(B/4)
"""
print(np.linalg.det(B/4))
"""
    det(C)
"""
print(np.linalg.det(C))
"""
    det(2B+C)
"""
print(np.linalg.det((2*B)+C))

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
def find_min(list) :
    temp= max(list)+1
    for i in range(len(list)) :
        if temp > list[i]:
            temp= list[i]
            postion = i
    return postion


#Part 3
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
print(selection_sort_as_seen_in_lectures([2,5,3,6,1]))

#Part 4
def selection_sort(list) :
    for n in range(len(list)) :
        minimum_list = list[n:len(list):1]
        minimum = find_min(minimum_list)
        Swap(list,minimum+n,n)
    return list

print(selection_sort([2,4,1,3,8]))

#Lab 6
#Part 1
def tuple_adder(tuple1, tuple2) :
    tuple_sum1 = np.array(tuple1)
    tuple_sum2 = np.array(tuple2)
    return_tuple = tuple_sum1+tuple_sum2
    return return_tuple
print(tuple_adder((1,2,3),(4,5,6)))

#part 2


#Lab 7
#Part 1

#Lab 8
#Part 1

#Part 2

#Lab 9
#Part 1

#Part 2











