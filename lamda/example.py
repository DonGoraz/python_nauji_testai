pairs = [(1, 10), (3, 6), (2, 9), (3, 8), (3, 6), (1, 8)]

print(sorted(pairs, key=lambda x: x))  # [(3, 8), (2, 9), (1, 10)]
print(min(pairs))  # (1, 10)

print(min(pairs, key=lambda x: x[1]))  # (1, 10)
print(max(pairs, key=lambda x: x[0] * x[1]))  # (3, 8)
