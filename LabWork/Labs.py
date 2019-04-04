import numpy as np
import matplotlib.pyplot as plot
import networkx as nx
import pulp

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

#Lab 8
#Part 1
problem = pulp.LpProblem("Simple problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x_1", lowBound=0, upBound=None, cat='Continuous')
x2 = pulp.LpVariable("x_2", lowBound=0, upBound=None, cat='Continuous')

objective = x1 + x2, "Objective function to maximize"
problem += objective

c1 = 2 * x1 + x2 <= 4, "First constraint"
c2 = x1 + 2 * x2 <= 3, "Second constraint"
problem += c1
problem += c2

print(problem)
problem.solve()
print("Optimal objective function = ", pulp.value(problem.objective))
for v in problem.variables():
    print(v.name, "=", v.varValue)

#Part 2
diet_Problem = pulp.LpProblem("Cat diet problem", pulp.LpMinimize)
x1 = pulp.LpVariable("Chicken Percentage", lowBound=0)
x2 = pulp.LpVariable("Beef Percentage", lowBound=0)
objective = 0.013 * x1 + 0.008 * x2, "Total cost over weight per can"
diet_Problem += objective
c1 = x1 + x2 == 100, "Percentage"
c2 = 0.07 * x1 + 0.2 * x2 >= 8, "LB on protein"
c3 = 0.08 * x1 + 0.1 * x2 >= 6, "LB on fat"
c4 = 0.001 * x1 + 0.005 * x2 <= 2, "UB on fibers"
c5 = 0.002 * x1 + 0.005 * x2 <= 0.4, "UB on salt"
diet_Problem += c1
diet_Problem += c2
diet_Problem += c3
diet_Problem += c4
diet_Problem += c5
print(diet_Problem)
diet_Problem.solve()
print(pulp.LpStatus[diet_Problem.status])
print(pulp.value(diet_Problem.objective) )
for v in diet_Problem.variables():
    print (v.name, "=", v.varValue, "%")
#Lab 9
#Part 1
"""
    Parameters
    ----------
        tableau : numpy.array with dtype=numpy.float64
                  initial tableau; it must be basic feasible
     Returns
     -------
        tableau : numpy.array with dtype=numpy.float64
                  final (basic feasible) tableau
        status : string
                 status of the problem: "unbounded" or "optimal"
        z : numpy.float
            optimal solution value (consistent only if status == "optimal")
    Notes
    -----
        The supplied tableau must be basic feasible.
"""
def simplex_method(tableau):
    print('Initial tableau')
    print(tableau)
    n = tableau.shape[1] - 1 # Number of variables (column 0 is ignored)
    m = tableau.shape[0] - 1 # Number of constraints (row 0 is ignored)

    while True:
        candidate_cols = \
            [col_idx for col_idx in range(1, n+1) if tableau[0, col_idx] < 0]
        s = candidate_cols[0] # Applying Bland's rule, the 1st column is chosen
        candidate_rows = \
            [row_idx for row_idx in range(1, m+1) if tableau[row_idx, s] > 0]
        if len(candidate_rows) == 0 :
            return "unbounded", float('inf'), numpy.zeros(n)
    # Min ratio test
        min, r = float('inf'), -1
        for i in candidate_rows:
            ratio = tableau[i,0] / tableau[i,s]
            if ratio < min: #By using '<', Bland's rule is automatically applied
                min, r = ratio, i
        print('Pivoting on (', r, ',', s, ')')
    # Rescale pivot row
        tableau[r, :] /= tableau[r, s]
    # Remove all entries in column s except for the pivot row
        for row in range(0, r):
            tableau[row, :] -= tableau[row, s] * tableau[r, :]
        for row in range(r+1, m+1):
            tableau[row, :] -= tableau[row, s] * tableau[r, :]
        print('Current tableau\n', tableau)
        if np.min([tableau[0,j] for j in range(1,n+1)]) >= 0:
            #if numpy.min(tableau[0, 1:] >= 0:
            break #Leave the while loop if all reduced costs are >= 0
    print("Optimal solution found")
    z = -tableau[0, 0]

    return tableau, "optimal", z


tableau = np.array([ [0, -1, -1, 0, 0],
                                 [4,  2,  -1, 1, 0],
                                 [3,  1,  2, 0, 1] ], dtype=np.float64)
final_tableau, status, z = simplex_method(tableau)
print("Final tableau =\n", final_tableau)
print("Status = ", status)
print("Optimal solution value =", z)
