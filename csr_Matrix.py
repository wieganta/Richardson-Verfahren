from vector import *
class csr_matrix:

    def __init__(self, csr_tup):

        self.data = csr_tup[0]
        self.indices = csr_tup[1]
        self.indptr = csr_tup[2]

    def __matmul__(self, x: vector):
        m = len(self.indptr) - 1
        b = [0] * m
        vector(b)
        for i in range(m):
            intervall = self.indptr[i:i + 2]
            for j in range(intervall[0], intervall[1]):
                b[i] = b[i] + self.data[j] * x[self.indices[j]]

        return b


class csr_tridiagonal:
    def __init__(self, a, b, c, n):
        self.data = [b, c]
        self.indices = [0, 1]
        self.indptr = [0, 2]

        indice_1 = 0
        indice_2 = 1
        indice_3 = 2

        for i in range(n - 2):
            self.data.append(a)
            self.data.append(b)
            self.data.append(c)
            self.indices.append(indice_1)
            self.indices.append(indice_2)
            self.indices.append(indice_3)

            indice_1 += 1
            indice_2 += 1
            indice_3 += 1

        self.data.append(a)
        self.data.append(b)
        self.indices.append(n - 2)
        self.indices.append(n - 1)

        last_indptr = 3 * n - 2
        second_last_indptr = 3 * n - 4
        indices = list(range(5, second_last_indptr, 3))

        for elem in indices:
            self.indptr.append(elem)

        self.indptr.append(second_last_indptr)
        self.indptr.append(last_indptr)

    def __matmul__(self, x: vector):
        m = len(self.indptr) - 1
        b = [0] * m
        vector(b)
        for i in range(m):
            intervall = self.indptr[i:i + 2]
            for j in range(intervall[0], intervall[1]):
                b[i] = b[i] + self.data[j] * x[self.indices[j]]

        return b


class dense_to_csr:
    def __init__(self, A):
        self.data = []
        self.indices = []
        self.indptr = [0]
        iter_indptr = 0

        for i in range (len(A)):
            for j in range(len(A)):
                if A[i][j] != 0:
                    iter_indptr += 1
                    self.data.append(A[i][j])
                    self.indices.append(j)

            self.indptr.append(iter_indptr)

    def __matmul__(self, x: vector):
        m = len(self.indptr) - 1
        b = [0] * m
        vector(b)
        for i in range(m):
            intervall = self.indptr[i:i + 2]
            for j in range(intervall[0], intervall[1]):
                b[i] = b[i] + self.data[j] * x[self.indices[j]]

        return b