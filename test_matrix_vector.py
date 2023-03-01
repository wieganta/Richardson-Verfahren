from csr_Matrix import *
from vector import *

data = [1,3,2,-1,4,5]
indices = [0,3,1,3,0,1]
indptr = [0,2,3,4,6]

tupel = (data,indices,indptr)
matrix_B = csr_matrix(tupel)

#--------------------
A = [[1,0,0,3],[0,2,0,0],[0,0,0,-1],[4,5,0,0]]
matrix_A = dense_to_csr(A)

x = [1,1,1,1]
y = [0,0,0,0]
z = [4,1,3,9]

x_1 = matrix_A @ x
y_1 = matrix_A @ y
z_1 = matrix_A @ z

print(x_1)
print(y_1)
print(z_1)

x_1 = matrix_B @ x
y_1 = matrix_B @ y
z_1 = matrix_B @ z

print(x_1)
print(y_1)
print(z_1)

e = vector([1,2,3,4])
print(e.euklidische_norm_quadrat())