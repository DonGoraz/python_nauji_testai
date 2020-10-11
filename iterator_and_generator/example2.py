from math import sqrt
import time

def laikas(n):
    def timer(fc):
        def wrapper(*args, **kwargs):
            start = time.time()
            rv = fc(n)
            total = time.time() - start
            print("Time:", total)
            return rv
        return wrapper
    return timer



def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeIterator:
    # Iterator that allows you to iterate over n primes
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    @laikas
    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


iter = PrimeIterator(100)
for elem in iter:
    print(elem)