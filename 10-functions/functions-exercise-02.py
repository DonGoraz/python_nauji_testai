def print_rectangle(n, symbl='#'):
    return (f"{symbl * n}\n" * n)[:-1]

var = int(input("Įveskite kraštinės ilgį: "))
print(print_rectangle(var, "#"))