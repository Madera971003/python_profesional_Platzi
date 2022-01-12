import time

class FiboIter:

    # Constructor
    def __init__(self, num_max: int = None):
        self.num_max = num_max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self # Retorna al objeto en sí mismo

    def __next__(self):
        if self.counter == 0:
            self.counter +=1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            if self.aux >= self.num_max:
                raise StopIteration
            # Resolviendo con soaping
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

# 0 1 1 2 3 5 8 13 21 34 55 89 ...

if __name__ == '__main__':
    fibonacci = FiboIter(1000)

    for element in fibonacci:
        print(element)
        time.sleep(0.5)