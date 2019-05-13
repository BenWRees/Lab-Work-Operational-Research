import numpy
import math1058_cwk

"""
    Description:
        Applies Dijkstra's Algortihm with O(n^3) complexity, the Algortihm
        goes from the starting_Node to the largest value node in the graph
    Parameter:
        successors - list of dictionaries for where for each dictionary
                     represents a node i, and all the outgoing arcs from the
                     node i, with the key representing which node an outgoing arc
                     is going to, and the corresponding value represents the
                     weight of the arc going from node i to the node in the key

        starting_Node - integer taken from the a dictionary which is where the
                        Algortihm starts and the  Algortihm chooses as the node
                        to begin at. Successors[starting_Node] is the dictionary
                        which contains the outgoing arcs from the starting_Node
    Returns:
        Returns a dictionary that is the path the Algortihm takes from the
        starting_Node to the largest value node in the graph, where the keys
        are the node values, and the values are the cumulative weight of the path
        at that node from the starting_Node
"""
#NOT CHECKING NUMBERS Less than s
"""
def dijkstra1(successors, s):
    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    distance = []
    while len(S) < n :
        for i in S :
            for j, length_ij in successors[i].items() :
                if length_ij == min(list(successors[i].values())) :
                    w = j
                    L[w] = L[i]+length_ij #E0 =2
                    P[w]=i #EO = 3
        S.append(w)#EO=4


    return L,P
"""

def  dijkstra1(successors,s) :
    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    minlength_j = numpy.inf
    #lines 59-75 is O(n^3)
    while len(S) < n :
        for i in S :
            for j, length_ij in successors[i].items() :
                if j in S :
                    continue
                elif L[i] + length_ij < minlength_j :
                    minlength_j = L[i] + length_ij
                    w = j
                    v = i
                else :
                    pass
                L[w] = minlength_j
                P[w] = v
                minlength_j = numpy.inf
                S.append(w)
                if len(S) == n :
                    return L,P



"""
    Description:
        Applies Dijkstra's Algortihm with O(n^2) complexity, the Algortihm
        goes from the starting_Node to the largest value node in the graph
    Parameter:
        successors - list of dictionaries for where for each dictionary
                     represents a node i, and all the outgoing arcs from the
                     node i, with the key representing which node an outgoing arc
                     is going to, and the corresponding value represents the
                     weight of the arc going from node i to the node in the key

        starting_Node - integer taken from the a dictionary which is where the
                        Algortihm starts and the  Algortihm chooses as the node
                        to begin at. Successors[starting_Node] is the dictionary
                        which contains the outgoing arcs from the starting_Node
    Returns:
        Returns a dictionary that is the path the Algortihm takes from the
        starting_Node to the largest value node in the graph, where the keys
        are the node values, and the values are the cumulative weight of the path
        at that node from the starting_Node
"""
def dijkstra2(successors, s):
    S = []
    S.append(s)
    n = len(successors)
    L = dict()
    L[s] = 0
    P = dict()
    P[s] = '-'
    V = []
    for i in range(0, n):
        V.append(i)
    V.remove(s)
    for i in range(0,n):
        if i in successors[s].keys():
            L[i] = successors[s][i]
            P[i] = s
        else:
            L[i] = numpy.inf
            P[i] = '-'

    L[s] = 0
    P[s] = '-'

    while len(S) < n:
        wlength = numpy.inf
        wnode = 0
        for i in V:
            if L[i] <= wlength:
                wlength = L[i]
                wnode = i
        S.append(wnode)
        V.remove(wnode)
        for j, lij in successors[wnode].items():
            if L[wnode]+lij < L[j]:
                L[j] = L[wnode]+lij
                P[j] = wnode
    return L,P


if __name__ == "__main__":
    adj1 = [{1 : 2, 2 : 5},
            {2 : 3},
            {3 : 4},
            {0 : 21, 1 : 8}]

    print(dijkstra2(adj1, 0))
    for o in range(0, 4):
        print(o)
        print(dijkstra1(adj1, o))
        print(dijkstra2(adj1, o))


        graph_ns, graph_ms, times = math1058_cwk.run_experiments(dijkstra1, 30643996)
        graph_ns, graph_ms, times = math1058_cwk.run_experiments(dijkstra2, 30643996)
