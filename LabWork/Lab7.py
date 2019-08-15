import networkx as nx
import matplotlib.pyplot as plot

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
plot.show()
