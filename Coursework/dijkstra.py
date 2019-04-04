import networkx as nx
import numpy as np
import xlwt

#dijkstra's Algortihm for O(n^3)
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
def dijkstra1(successors, current_Node) :
    path_taken = dict()
    #wish to only undergo the algorithm if there are any nodes that need to be
    #checked in the graph
    while len(successors) > 0 :
        #wish to check through the outgoing arcs from our current_Node
        """
        check the weights of the current_Node to see  which is the lowest
        """
        for key,value in successors[current_Node] :



#dijkstra's Algortihm for O(n^2)
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
def dijkstra2(successors, starting_Node) :
    return null
