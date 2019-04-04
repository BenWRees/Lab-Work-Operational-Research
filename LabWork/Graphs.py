import matplotlib.pyplot as plot
import numpy as np
import networkx as nx

#Lab 5

#Part 1 - NEED TO ADD LEGENDS
domain1 = np.linspace(0.0,1.0, num=20)
for s in range(2,6) :
    codomain1 = domain1**s
    codomain2 = domain1**(s**-1)
    plot.xlabel("Domain")
    plot.ylabel("Image")
    #plot.legend("x^2","x^3","x^4")
    plot.plot(domain1, codomain1)
    plot.plot(domain1, codomain2)
plot.show()

#Part 2 - Ask for Help (what does it mean, 'from above'?)
#First produce a single figure with two subplots:
domain = np.linspace(0.0,1.0, num=20)
f, axarr = plot.subplots(2, sharex=True)
plot.xlabel("Domain")
plot.ylabel("Image")
for s in range(2,6) :
    codomain1 = domain1**s
    #plot.legend("x^2","x^3","x^4")
    axarr[0].plot(domain1, codomain1)
    for s in range(2,6) :
        codomain2 = domain1**(s**-1)
        axarr[1].plot(domain1, codomain2)
plot.show()
"""
Second produce a single figure with eight subplots, one
for each curve.
"""
domain = np.linspace(0.0,1.0, num=20)
f, axarr = plot.subplots(8, sharex=True,squeeze=True)
plot.xlabel("Domain")
plot.ylabel("Image")
for s in range(2,6) :
    codomain1 = domain1**s
    #plot.legend("x^2","x^3","x^4")
    axarr[s].plot(domain1, codomain1)
    codomain2 = domain1**(s**-1)
    axarr[s].plot(domain1, codomain2)
plot.show()
#Part 3
"""
    Trying out the loglog function - takes the logarithm of the image and domain
    """
domain2 = np.linspace(10**(-5),1.0, num=20)
for s in range(2,6) :
    codomain1 = domain2**s
    codomain2 = domain2**(s**-1)
    plot.xlabel("Domain")
    plot.ylabel("Image")
    #plot.legend("x^2","x^3","x^4")
    plot.loglog(domain2, codomain1)
    plot.loglog(domain2, codomain2)
plot.show()
"""
    Trying out the semilogx function - takes the logarithm of only the domain
    """
for s in range(2,6) :
    codomain1 = domain2**s
    codomain2 = domain2**(s**-1)
    plot.xlabel("Domain")
    plot.ylabel("Image")
    #plot.legend("x^2","x^3","x^4")
    plot.semilogx(domain2, codomain1)
    plot.semilogx(domain2, codomain2)
plot.show()
"""
    Trying out the semilogy function - takes the logarithm of only the image
    """
for s in range(2,6) :
    codomain1 = domain2**s
    codomain2 = domain2**(s**-1)
    plot.xlabel("Domain")
    plot.ylabel("Image")
    #plot.legend("x^2","x^3","x^4")
    plot.semilogy(domain2, codomain1)
    plot.semilogy(domain2, codomain2)
plot.show()
"""
    Trying out the xscale function - sets the scaling of only the x-axis to scale logarithmically
    """
for s in range(2,6) :
    codomain1 = domain2**s
    codomain2 = domain2**(s**-1)
    plot.xlabel("Domain")
    plot.ylabel("Image")
    plot.xscale('log')
    #plot.legend("x^2","x^3","x^4")
    plot.plot(domain2, codomain1)
    plot.plot(domain2, codomain2)
plot.show()

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
