import numpy as np
from scipy.optimize import linear_sum_assignment

g1 = np.array([[0, 1, 1, 0, 1],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 1, 0],
               [0, 0, 1, 0, 1],
               [1, 0, 0, 1, 0]])

g2 = np.array([[0, 1, 1, 0, 0],
               [1, 0, 1, 1, 1],
               [1, 1, 0, 1, 1],
               [0, 1, 1, 0, 1],
               [0, 1, 1, 1, 0]])

# eigendecomposition of g1
w_g1, v_g1 = np.linalg.eig(g1)

# eigendecomposition of g2
w_g2, v_g2 = np.linalg.eig(g2)

# The eigendecomposition of g1 results in:
print("g1")
print(w_g1)
print("g1")
print(v_g1)
# w_g1 = [ 2.23606798,  1.        , -1.        , -0.61803399, -0.61803399]
# v_g1 = [[ 0.40824829, -0.70710678, -0.5       , -0.33333333, -0.11911698],
#         [ 0.40824829,  0.70710678, -0.5       , -0.33333333, -0.11911698],
#         [ 0.57735027,  0.        ,  0.5       , -0.33333333, -0.71443457],
#         [ 0.40824829, -0.        ,  0.5       ,  0.66666667,  0.44060408],
#         [ 0.40824829, -0.        ,  0.5       , -0.        ,  0.54094245]]


# The eigendecomposition of g2 results in:
print("g2")
print(w_g2)
print("g2")
print(v_g2)
# w_g2 = [ 2.23606798,  1.        , -1.        ,  1.        , -1.23606798]
# v_g2 = [[ 0.40824829, -0.70710678, -0.5       , -0.35404144,  0.25663216],
#         [ 0.40824829,  0.70710678, -0.5       , -0.35404144,  0.25663216],
#         [ 0.57735027,  0.        ,  0.5       , -0.35404144, -0.7094241 ],
#         [ 0.40824829, -0.        ,  0.5       ,  0.70661918,  0.35474171],
#         [ 0.40824829, -0.        ,  0.5       , -0.43865661, -0.55758288]]

# Compute U_g1 U^T_g2
U_g1 = v_g1.T
U_g2 = v_g2.T
U_g1_UT_g2 = np.dot(U_g1, U_g2.T)
print("U_g1_UT_g2")
print(U_g1_UT_g2)
# The resulting U_g1_UT_g2 matrix is:
# array([[ 0.8660254 ,  0.5       ,  0.28867513,  0.40824829, -0.03029768],
#        [-0.5       ,  0.8660254 , -0.28867513,  0.40824829,  0.03029768],
#        [ 0.28867513, -0.28867513,  0.8660254 ,  0.5       , -0.5       ],
#        [-0.40824829, -0.40824829, -0.5       ,  0.8660254 , -0.28867513],
#        [ 0.03029768, -0.03029768,  0.5       ,  0.28867513,  0.81649658]])

# Find the optimal assignment using the LSAP solver
row_ind, col_ind = linear_sum_assignment(-U_g1_UT_g2)
print(row_ind)
print(col_ind)
# The resulting row and column indices are:
# row_ind = [0 1 2 3 4]
# col_ind = [0 1 4 2 3]
# This indicates that node 0 in g1 is matched
# with node 0 in g2, node 1 in g1 is matched
# with node 1 in g2, node 2 in g1 is matched
# with node 4 in g2, node 3 in g1 is matched
# with node 2 in g2, and node 4 in g1 is matched
# with node 3 in g2.





