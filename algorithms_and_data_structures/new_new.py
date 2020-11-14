# n = int(input())
#
# i = 1
# s = 1
#
# while i <= n:
#     s = s * i
#     i = i + 1
#
# print(s)
#
#
# d = int(input())
# bbb = bin()
#
#
# r = d % 2
# if r == 1:

# d = int(input())
#
#
# def convert(number):
#     if number >= 0:
#         bs = list()
#         while number != 0:
#             r = number % 2
#             if r == 1:
#                 bs.append(1)
#             else:
#                 bs.append(0)
#
#             number = number // 2
#
#             if number == 0:
#                 return bs[::-1]
#
#
# print(convert(d))


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# else:
#     print(a)


s = "Zmogus nuejo i Regitra uzregistruoti savo BMW. Bet pasirodo, kad JTO uzdraude BMW automobilius."

print(s.strip('.,*-'))


# listas = list(s.split("."))
#
# print(listas)
# for _ in listas:
#     if _[0].isupper():
#         print(_)
#

for sakinys in s.split('.'):
    for zodis in sakinys.split(' '):
        if sakinys.index(zodis) > 1 and zodis.istitle():
            print(zodis)
        if zodis.isupper():
            print(zodis)