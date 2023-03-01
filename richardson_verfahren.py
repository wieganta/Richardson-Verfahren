from vector import *
from csr_Matrix import *

def richardson_verfahren (A,b,x,theta,maxiter,tol):
    matrix_a = csr_matrix(A)
    vec_b = vector(b)
    vec_x = vector(x)
    r_k = 0
    tol_quadrat = tol ** 2
    r_k_liste = []

    for k in range(maxiter):
        r_k = (matrix_a @ vec_x) - b
        r_k_liste.append(r_k.euklidische_norm_quadrat())
        if r_k.euklidische_norm_quadrat() < tol_quadrat:
            break
        vec_x = vec_x - (theta * r_k)

    return vec_x, k, r_k.euklidische_norm_quadrat(), #r_k_liste

