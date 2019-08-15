import numpy as np

#Lab 9
#Part 1
"""
    Parameters
    ----------
        tableau : numpy.array with dtype=numpy.float64
                  initial tableau; it must be basic feasible
     Returns
     -------
        tableau : numpy.array with dtype=numpy.float64
                  final (basic feasible) tableau
        status : string
                 status of the problem: "unbounded" or "optimal"
        z : numpy.float
            optimal solution value (consistent only if status == "optimal")
    Notes
    -----
        The supplied tableau must be basic feasible.
"""
def simplex_method(tableau):
    print('Initial tableau')
    print(tableau)
    n = tableau.shape[1] - 1 # Number of variables (column 0 is ignored)
    m = tableau.shape[0] - 1 # Number of constraints (row 0 is ignored)

    while True:
        candidate_cols = \
            [col_idx for col_idx in range(1, n+1) if tableau[0, col_idx] < 0]
        s = candidate_cols[0] # Applying Bland's rule, the 1st column is chosen
        candidate_rows = \
            [row_idx for row_idx in range(1, m+1) if tableau[row_idx, s] > 0]
        if len(candidate_rows) == 0 :
            return "unbounded", float('inf'), numpy.zeros(n)
    # Min ratio test
        min, r = float('inf'), -1
        for i in candidate_rows:
            ratio = tableau[i,0] / tableau[i,s]
            if ratio < min: #By using '<', Bland's rule is automatically applied
                min, r = ratio, i
        print('Pivoting on (', r, ',', s, ')')
    # Rescale pivot row
        tableau[r, :] /= tableau[r, s]
    # Remove all entries in column s except for the pivot row
        for row in range(0, r):
            tableau[row, :] -= tableau[row, s] * tableau[r, :]
        for row in range(r+1, m+1):
            tableau[row, :] -= tableau[row, s] * tableau[r, :]
        print('Current tableau\n', tableau)
        if np.min([tableau[0,j] for j in range(1,n+1)]) >= 0:
            #if numpy.min(tableau[0, 1:] >= 0:
            break #Leave the while loop if all reduced costs are >= 0
    print("Optimal solution found")
    z = -tableau[0, 0]

    return tableau, "optimal", z


tableau = np.array([ [0, -1, -1, 0, 0],
                                 [4,  2,  -1, 1, 0],
                                 [3,  1,  2, 0, 1] ], dtype=np.float64)
final_tableau, status, z = simplex_method(tableau)
print("Final tableau =\n", final_tableau)
print("Status = ", status)
print("Optimal solution value =", z)
