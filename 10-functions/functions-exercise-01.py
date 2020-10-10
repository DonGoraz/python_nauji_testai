# def  maÿ_of_three(a, b, c):
#     if a > b:
#         big = a
#     else:
#         big = b
#
#     if big > c:
#         return big
#     else:
#         big = c
#         return big
#
# a = input("Iveskite skaiciu: ")
# b = input("Iveskite skaiciu: ")
# c = input("Iveskite skaiciu: ")
#
# print(maÿ_of_three(int(a), int(b), int(c)))


def max_of_three (a,b,c):
    return max(a, b, c)

a = int(input("Iveskite skaiciu a: "))
b = int(input("Iveskite skaiciu b: "))
c = int(input("Iveskite skaiciu c: "))

print(f"Didziausiais skaicius yra: {max_of_three(a,b,c)}")