class vector(list):

    def __add__(self, others):
        return vector([sum(i) for i in zip(self, others)])

    def __sub__(self, others):
        return vector([i - j for i, j in zip(self, others)])

    def __mul__(self, others):
        return vector([i * others for i in (self)])

    def __rmul__(self, others):
        return vector([i * others for i in (self)])

    def euklidische_norm_quadrat(self):
        summe = 0

        for i in (self):
            summe += i ** 2

        return summe
