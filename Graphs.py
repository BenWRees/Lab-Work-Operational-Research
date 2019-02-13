import matplotlib.pyplot as plot

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
