"""
    Description:
         function that converts a graph representation from
         successors list to incidence matrix.
    Parameter:
        list - a successors list, defined as a list of lists
        where each sublist of index i contains the indices of the nodes that
        can be reached from i via a single arc
    Returns:
        a single list containing all the node indices in the graph,
        and a binary matrix, implemented as a numpy.ndarray, corresponding to the
        incidence matrix of the graph, with a 1 in position i,j if and only
        if there is an arc between i and j
"""
def to_nx_graph(list) :
