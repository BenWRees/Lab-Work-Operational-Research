import numpy as np

"""
    Description:
         function that converts a graph representation from
         successors list to incidence matrix.
    Parameter:
        successors - a successors list, defined as a list of lists
                            where each sublist of index i contains the indices
                            of the nodes that can be reached from i via a single arc
    Returns:
        a single list containing all the node indices in the graph,
        and a binary matrix, implemented as a numpy.ndarray, corresponding to the
        incidence matrix of the graph, with a 1 in position i,j if and only
        if there is an arc between i and j
"""
def to_nx_graph(successors) :
    nodes = []
    incidenceMatrix = np.zeros(shape = (len(successors), len(successors)))
    #on the assumption that nodes will be in linear ascending order starting at 0
    """
    could we loop though looking at each sub-list and then looping through each
    sub-list checking if an element exists in the array nodes, if not placing
    it in the array??
    """
    for i in range(len(successors)) :
        nodes.append(i)
        for j in range(len(successors[i])) :
            incidenceMatrix[i][successors[i][j]] = 1
    return nodes, incidenceMatrix



"""
    Description:
         calculates the out and in degrees of all nodes of a successors list
    Parameter:
        successors - a successors list, defined as a list of lists
                            where each sublist of index i contains the indices
                            of the nodes that can be reached from i via a single arc
    Returns:
        returns two lists containing, in order of node index, the out-degrees and
        in-degrees of all the nodes: that is, the number of arcs contained in
        the forward start of each node in one list and the number of arcs
        contained in the backward start of each node in the other lis
"""
def node_degree(successors) :
    outDegree = list()
    inDegree = list()
    nodes = list()
    flatsuccessors =list()
    for node in range(len(successors)) :
        nodes.append(node)
    for subList in successors :
        outDegree.append(len(subList))
        for value in subList :
            flatsuccessors.append(value)
    for value in nodes :
        inDegree.append(flatsuccessors.count(value))

    return outDegree, inDegree


#print(node_degree([[1,2],[2],[],[0,1]]))

"""
    Description:
         checks if every node can be reached from 0
    Parameter:
        successors - a successors list, defined as a list of lists
                            where each sublist of index i contains the indices
                            of the nodes that can be reached from i via a single arc
    Returns:
        returns boolean depending if every node can be reached from 0
            True  - if every node can be  reached from  0
            False - if not every node can be reached from  0
"""
def reachability(successors) :
    reachableNodes =  list()
    reachableNodes.append(0)
    path = list()
    nodes = list()
    #building node list for comparision
    for node in range(len(successors)) :
        nodes.append(node)
    #adding all the nodes that are connected to 0
    for explored in successors[0] :
        reachableNodes.append(explored)
        path.append(explored)

    #checking all the nodes in the path to 0
    for pathNode in path : #loop through the nodes currently in the path
        for explored in successors[pathNode] :
            if explored not in reachableNodes :
                reachableNodes.append(explored)
                path.append(explored)

    #checks if all the nodes in reachable nodes are all the nodes in the graph
    if set(nodes) == set(reachableNodes) :
        return True
    else :
        return False

print(to_nx_graph([[1,2],[2],[],[0,1]]))
print(node_degree([[1,2],[2],[],[0,1]]))
print(reachability([[1,2],[2],[],[0,1]]))
