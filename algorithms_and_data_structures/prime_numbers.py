# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return n
# print(test_prime(5))

# num = 11
#
# # If given number is greater than 1
# if num > 1:
#
#     # Iterate from 2 to n / 2
#     for i in range(2, num):
#
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")


# prime_numbers = 0
#
# def is_prime_number(x):
#     if x >= 2:
#         for y in range(2, x):
#             if not (x % y):
#                 return False
#     else:
#         return False
#     return True
#
#
# for i in range(int(input("How many numbers you wish to check: "))):
#     if is_prime_number(i):
#         prime_numbers += 1
#         print(i)
#
# print("We found " + str(prime_numbers) + " prime numbers.")


# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)
#
# print(prime_eratosthenes(100));


def erathostene(n):
    numbers = []
    primer_numbers = []
    for i in range(2, n+1):
        numbers.append(i)
    primer_numbers = numbers

    for number in numbers:
        for pr_number in primer_numbers:
            if (pr_number % number == 0) and (pr_number != number):
                primer_numbers.remove(pr_number)

    print(primer_numbers)

erathostene(100)

