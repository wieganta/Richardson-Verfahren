from vector import *

class csr_matrix:

    def __init__(self, csr_tup):

        self.data = csr_tup[0]
        self.indices = csr_tup[1]
        self.indptr = csr_tup[2]

    def __matmul__(self, x: vector):
        m = len(self.indptr) - 1
        b = [0] * m

        for i in range(m):
            intervall = self.indptr[i:i + 2]
            for j in range(intervall[0], intervall[1]):
                b[i] = b[i] + self.data[j] * x[self.indices[j]]

        return vector(b)


    def csr_tridiagonal(tupel,n):
        a = tupel[1]
        b = tupel[2]
        c = tupel[3]

        data = [b, c]
        indices = [0, 1]
        indptr = [0, 2]

        indice_1 = 0
        indice_2 = 1
        indice_3 = 2

        for i in range(n - 2):
            data.append(a)
            data.append(b)
            data.append(c)
            indices.append(indice_1)
            sindices.append(indice_2)
            sindices.append(indice_3)

            indice_1 += 1
            indice_2 += 1
            indice_3 += 1

        data.append(a)
        data.append(b)
        indices.append(n - 2)
        indices.append(n - 1)

        last_indptr = 3 * n - 2
        second_last_indptr = 3 * n - 4
        indices = list(range(5, second_last_indptr, 3))

        for elem in indices:
            indptr.append(elem)

        indptr.append(second_last_indptr)
        indptr.append(last_indptr)

        return(data,indices,indptr)

    def dense_to_csr(A):

        data = []
        indices = []
        indptr = [0]
        iter_indptr = 0

        for i in range (len(A)):
            for j in range(len(A)):
                if A[i][j] != 0:
                    iter_indptr += 1
                    data.append(A[i][j])
                    indices.append(j)

            indptr.append(iter_indptr)

        return (data, indices, indptr)