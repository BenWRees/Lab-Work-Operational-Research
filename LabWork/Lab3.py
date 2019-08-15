import numpy as np

#Lab 3
#Part 1
"""
    Description:
        Does one step of gaussian elimination in bringing a matrix to upper triangular
    Parameters:
        A - multi-dimensional Array that acts as a matrix
        r1 - integer value that represents the row that is being replaced
        r2 - integer value of row that is taking away from row being replaced
    Returns:
        Matrix that has undergone one step of gaussian elimination closer to upper triangular form
"""

def Row_Elimination(A, r1, r2) :
    e = (A[r2][0])/(A[r1][0])
    A[r2] = A[r2] - e*A[r1]
    return A
print(Row_Elimination(A,2,1))

#Part 2 - NEED TO FIX ALL BUT DET(C) and Det(B/4)
"""
    det((A^T)(B^-1))
"""
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_B_inverse = (det_B)**(-1)
det_total = det_B_inverse*det_A
print(det_total)
"""
    det(B/4)
"""
constant = (0.25)**4
determinant = float(constant*np.linalg.det(B))
print(determinant)
"""
    det(C)
"""
print(np.linalg.det(C))
"""
    det(2B+C)
"""
matrix_2B = 2*B
matrix_2BC = matrix_2B+C
det_Matrix_2BC = float(np.linalg.det(matrix_2BC))
print(det_Matrix_2BC)
