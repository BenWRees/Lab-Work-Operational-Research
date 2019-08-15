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
