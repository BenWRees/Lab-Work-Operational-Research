import numpy as np

#Lab 2
#Part 1
"""
    Description:
        flips a string in reverse order
    Parameters:
        s - string that will be flipped into reverse order
    Returns:
        a string that is the reversed form of the parameter s
"""

def Flip(s) :
    temp=s[1:len(s):]
    temp=temp[::-1]
    s=s[0]+temp
    return s
print(Flip("abc"))

#Part 2

for n in [1.0,2.0,3.0,4.0,5.0] :
    print(1/(n**4))

#Part 3

summation = 0
for p in range(2,6) :
    for n in range(1,1000) :
        summation = n**(-p)
    print(summation)

#Lab 3
A = np.array([[1.0, 4.0, 3.0, 2.0],
                 [2.0, -7.0, 5.0, 1.0],
                 [1.0, 2.0, 6.0, 0.0],
                 [2.0, -10.0, 3.0, 4.0]])
B = np.array([[5.0, 2.0, -4.0, -2.0],
                 [-3.0, 1.0, 5.0, 1.0],
                 [4.0, -1.0, 1.0, 3.0],
                 [2.0, 1.0, -1.0, 1.0]])
C = np.array([[3.0, 0.0, 0.0, 0.0],
                 [7.0, -6.0, 0.0, 0.0],
                 [2.0, -1.0, -1.0, 0.0],
                 [-4.0, -2.0, 2.0, -2.0]])
