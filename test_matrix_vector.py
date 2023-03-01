from csr_Matrix import *
from vector import *
from richardson_verfahren import *

#Richardson_verfahren:

data = [1,2,3,4]
indices = [0,1,2,3]
indptr = [0,1,2,3,4]
tupel = (data,indices,indptr)
b = [1,2,3,4]
x = [0,0,0,0]
tol =10 ** (-7)
theta = 0.2
maxiter = 1000
print("richardson_verfahren: ")
print(richardson_verfahren (tupel,b,x,theta,maxiter,tol))

#-------------------------------------------------------
#Richardson_verfahren_mit_tridiagonalmatrix:
tridiagonalmatrix = (2,3,2)
tupel = csr_tridiagonal(tridiagonalmatrix, 3)
b = [1,1,1]
x = [0,0,0]
tol =10 ** (-7)
theta = 0.17
maxiter = 10000
print("richardson_verfahren_tridiagonalmatrix: ")
print(richardson_verfahren (tupel,b,x,theta,maxiter,tol))

#-------------------------------------------------------
#Richardson_verfahren_mit_dense_to_csr:
A = [[2,1,0],[1,2,1],[0,1,2]]
tupel = dense_to_csr(A)
b = [4,4,4]
x = [0,0,0]
tol =10 ** (-7)
theta = 0.29
maxiter = 10000
print("richardson_verfahren_mit_dense_to_csr: ")
print(richardson_verfahren (tupel,b,x,theta,maxiter,tol))

#--------------------------------------------------------
# Test für Vektoren
def test_mul():
    assert vector([1, 2, 3, 4])*3 == vector([3, 6, 9, 12])
    assert vector([1, 1, 1, 3])*2 != vector([2, 1, 2, 6])
    assert vector([1, 2, 3, 4])*0 != vector([0])
    assert vector([3, 3, 3])*(1/3) == vector([1, 1, 1])
    assert vector([0, 0, 0, 0])*4 == vector([0, 0, 0, 0])

test_mul()


def test_rmul():
    assert 3*vector([1, 2, 3, 4]) == vector([3, 6, 9, 12])
    assert 2*vector([1, 1, 1, 3]) != vector([2, 1, 2, 6])
    assert 0*vector([1, 2, 3, 4]) == vector([0, 0, 0, 0])
    assert (1/3)*vector([9, 9, 9]) == vector([3, 3, 3])
    assert 11*vector([0, 0, 0, 0]) == vector([0, 0, 0, 0])

test_rmul()

def test_add():
    assert vector([1, 2, 3]) + vector([0, 1, 2]) == vector([1, 3, 5])
    assert vector([6]) + vector([3]) == vector([9])
    assert vector([0, 0, 0]) + vector([1, 2, 3]) == vector([1, 2, 3])
    assert vector([3, 3, 1]) + vector([1, 2, 1]) != vector([3, 3, 5])
    assert vector([-5, 3]) + vector([3, -2]) == vector([-2, 1])

test_add()

def test_sub():
    assert vector([1, 1, 1]) == vector([1, 2, 3]) - vector([0, 1, 2])
    assert vector([1, 2]) == vector([2, 4]) - vector([1, 2])
    assert vector([1, 3, 5, 3, 1]) == vector([3, 5, 7, 5, 3]) - vector([2, 2, 2, 2, 2])
    assert vector([2, 3, 5, 1]) == vector([5, 4, 8, 7]) - vector([3, 1, 3, 6])
    assert vector([6]) == vector([9]) - vector([3])

test_sub()

def test_norm():
    assert vector([3, 4]).euklidische_norm_quadrat() == 25
    assert vector([1, 2, 3]).euklidische_norm_quadrat() != 3
    #assert vector([0, 0, 0]).euklidische_norm_quadrat == 0
    assert vector([1, 1, 1, 1, 1, 1, 1, 1]).euklidische_norm_quadrat() == 8
    assert vector([3, 3]).euklidische_norm_quadrat() == 18

test_norm()

#----------------------------------------------------------------------
# Test für Matrizen
def test_matrix_vector_mul():
    data = [1,3,2,-1,4,5]
    indices = [0,3,1,3,0,1]
    indptr = [0,2,3,4,6]
    trippel = (data,indices,indptr)
    matrix_A = csr_matrix(trippel)
    vec_A = vector([1,1,1,1])
    vec_B = vector([2,0,1,3])

    assert vector([4,2,-1,9]) == matrix_A @ vec_A
    assert vector([11,0,-3,8]) == matrix_A @ vec_B

test_matrix_vector_mul()
