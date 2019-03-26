"""
    Take two lists list_1 and list_2. Using both zip (combines tuples together) and enumerate (prints out index and object) together, print (index, result) where index should count the entry into list_1 and result = list_1[index] + index * list_2[index].
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
