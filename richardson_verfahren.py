from vector import *
from csr_Matrix import *

def richardson_verfahren (A,b,x,theta,maxiter,tol):
    # matrix_a =
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