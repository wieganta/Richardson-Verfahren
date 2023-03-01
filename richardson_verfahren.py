from vector import *
from csr_Matrix import *

def richardson_verfahren (A,b,x,theta,maxiter,tol):
    matrix_a = csr_matrix(A)
    vec_b = vector(b)
    vec_x = vector(x)
    r_k = 0
    tol_quadrat = tol ** 2

    for k in range(maxiter):
        r_k = (matrix_a @ vec_x) - b
        if r_k.euklidische_norm_quadrat() < tol_quadrat:
            break
        vec_x = vec_x - (theta * vec_x)

    return vec_x

data = [1,2,2,1,1,2,2,2]
indices = [0,3,1,2,3,4,0,2]
indptr = [0,2,4,5,6,8]
tupel = (data,indices,indptr)
b = [1,2,0,1,1]
x = [0,0,0,0,0]
tol =10 ** (-6)
theta = 0.5
maxiter = 1000

richardson_verfahren (tupel,b,x,theta,maxiter,tol)
