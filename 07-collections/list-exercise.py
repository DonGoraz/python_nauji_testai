listas = [1, 2, 3, 4, 5]
print(listas)
print(len(listas))
listas.append(2)
print(listas.count(2))
print(listas.count(7))
listas.extend([6, 7, 8])
print(listas.index(7), listas[listas.index(7)])
listas.insert(0, 10)
print(listas[-1])
print(listas.pop())
print(listas)
listas.remove(4)
print(listas)
listas.reverse()
print(listas)
listas.sort()
print(listas)
listas.clear()
print(listas)