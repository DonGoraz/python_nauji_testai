# a = [1, 2, 3, 4]
# for item in a:
#     print(item)
#
# a = "Alice has a cat"
# for item in a:
#     print(item)
#
# a = {'name': "Adam", 'surname': "Smith"}
# for item in a:
#     print(item)


from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


lst = get_n_primes(1000000)
for elem in lst:
    print(elem)