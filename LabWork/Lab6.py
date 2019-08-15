import numpy as np

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
