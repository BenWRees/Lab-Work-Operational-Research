import numpy as np
import matplotlib.pyplot as plot
import networkx as nx

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
    e = (A[r2][0])/(A[r1][0])
    A[r2] = A[r2] - e*A[r1]
    return A
print(Row_Elimination(A,2,1))

#Part 2 - NEED TO FIX ALL BUT DET(C) and Det(B/4)
"""
    det((A^T)(B^-1))
"""
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_B_inverse = (det_B)**(-1)
det_total = det_B_inverse*det_A
print(det_total)
"""
    det(B/4)
"""
constant = (0.25)**4
determinant = float(constant*np.linalg.det(B))
print(determinant)
"""
    det(C)
"""
print(np.linalg.det(C))
"""
    det(2B+C)
"""
matrix_2B = 2*B
matrix_2BC = matrix_2B+C
det_Matrix_2BC = float(np.linalg.det(matrix_2BC))
print(det_Matrix_2BC)

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

#Lab 6
#Part 1
"""
    Description:
        adds two tuples of n length together using the module 'Numpy'

    Paramaters:
        tuple1 - a tuple of n length that will be added to another tuple
        tuple2 - a tuple of n length that will be added to tuple1

    Returns:
        a tuple of n length with the i-th element from each each tuple added together
"""
def tuple_adder(tuple1, tuple2) :
    tuple_sum1 = np.array(tuple1)
    tuple_sum2 = np.array(tuple2)
    return_tuple = tuple_sum1+tuple_sum2
    return return_tuple
print(tuple_adder((1,2,3),(4,5,6)))

#part 2
"""
    Description:
        finds the total weighting of a path in a graph

    Paramaters:
        graph - a dictionary that contains two nodes that create an arc as the key, and the weighting of the arc
        path - a tuple that contains the arcs that create a path

    Returns:
        an integer value that represents the total weighting of all the weights of each arc on the path added together

"""
def weight_of_path(graph,path) :
    total_weight = 0
    for i in path :
        additive_weight = graph[i]
        total_weight = total_weight + additive_weight
    return total_weight

graph = {(0,1):2, (1,0):3, (2,3):4, (1,2):6}
path = ((0,1), (1,2), (2,3))
print(weight_of_path(graph,path))
#part 3
"""
    Description:
        Take two lists list_1 and list_2. Using both zip (combines tuples together) and enumerate
        (prints out index and object) together, print (index, result) where index should count the
        entry into list_1 and result = list_1[index] + index * list_2[index].

    Paramaters:
        list_1 - a list of integer values
        list_2 - a list of integer values

    Returns:
        a tuple of the summation of all the index values in list_1 and the result of list_1[a] + (a*list_2[a])
        where 'a' represents the index of the two lists at that point
"""
def index_result_calculator(list_1,list_2) :
    index = 0
    count = 0
    for a, (x,y) in enumerate(zip(list_1,list_2)) :
        index = index + a
        count = list_1[a] + a*list_2[a]
    return index,count


list_1 = [1,2,2,3,4,2]
list_2 = [3,2,5,1,2,43,54,6,76]
print(index_result_calculator(list_1,list_2))

#Lab 7
#Part 1
distances = nx.DiGraph()
distances.add_node(1, city="Southampton")
distances.add_node(2, city="Brighton")
distances.add_node(3,city="London")
distances.add_node(4, city="Bath")
distances.add_node(5,city="Reading")
distances.add_node(6,city="Exeter")
distances.add_node(7,city="Salisbury")

distances.add_edge(1,2, distances="69")
distances.add_edge(1,3, distances="79")
distances.add_edge(1,4, distances="64")
distances.add_edge(1,5, distances="47")
distances.add_edge(1,6, distances="110")
distances.add_edge(1,7, distances="23")

plot.figure()
positions = nx.spring_layout(distances)
nx.draw(distances,positions, with_labesl=False)
nlabels=nx.get_node_attributes(distances, "city")
elabels=nx.get_edge_attributes(distances, "distances")
nx.draw_networkx_labels(distances,positions, labels=nlabels)
nx.draw_networkx_edge_labels(distances, positions, edge_labels= elabels)
#plot.title("Distances of various cities from Southampton")
plot.show()
#plot.savefig("Distances_of_various_cities_from_Southampton.png")


#Lab 8
#Part 1

#Part 2

#Lab 9
#Part 1

#Part 2
