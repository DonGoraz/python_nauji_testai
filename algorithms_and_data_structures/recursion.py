

# def factorial(n):
#     """Calculate factorial.
#
#     Args:
#         n: the natural number that is the input for the algorithm.
#     Returns:
#         factorial of number n.
#     """
#     print(f'input - n={n}')
#     if n == 0:
#         print(f'base case - n={n}')
#         return 1
#     else:
#         print(f'going deeper with {n-1}')
#         print(f'result {n * factorial(n-1)}')
#         return n * factorial(n-1)
#
#
def factorial(n, memory={0: 1, 1: 1, 2: 2, 3: 6, 5: 120, 6: 720, 9: 362880}):
    """Calculates factorial using dynamic programming.

    Args:
        n: the natural number that is the input for the algorithm.
        memory: the results dictionary will be updated with each function call.
    Returns:
        factorial of number n.
    """
    if n in memory:
        print(f'going deeper {memory[n]}')
        return memory[n]
    else:
        memory[n] = n * factorial(n-1)
        print(f'going deeper0 {memory[n]}')
        return memory[n]


n = int(input('iveskite skaiciu: '))

print(f'rezultatas: {factorial(n)}')

