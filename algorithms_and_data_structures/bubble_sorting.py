import random

lst = [random.randint(0, 10) for i in range(10)]

# daug pvz https://www.programcreek.com/python/?CodeExample=bubble+sort
# # lst = [9,4,5,6,7,2,1]
# print(lst)
#
# # for i in lst:
#     # print(i)
#     # print(i-1)
#
#
# for i in range(len(lst)):
#     print("-1 = ", lst[i - 1])
#     print("dabar ", lst[i])
#     print("+1 = ", lst[i + 1])


# Gedas

# import random
# #
# lst = [random.randint(0, 10) for i in range(random.randint(1,50))]
# #lst = [1, 6, 8, 5, 0]
# print(lst)
# swap = True
# while swap :
#     swap = False
#     for i in range(0, len(lst)-1):
#         if lst[i] > lst[i+1]:
#             lst[i+1], lst[i] = lst[i], lst[i+1]
#             swap = True
# print(lst)

# Irmantas
# lst = [5, 4, 3, 2, 1]
# l = len(lst)
#
# no_swap = 0
# while no_swap < (l - 1):
#     for i in range(l - 1):
#         swap = 0
#         if lst[i] < lst[i + 1]:
#             no_swap += 1
#         else:
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
#             swap += 1
#     print(lst)
#
# print(lst)


# Mantas
# def bubbleSort(lst):
#     n = len(lst)
#     swapNumber = 0
#     for i in range(n):
#         swapped = False
#
#         for j in range(0, n - i - 1):
#
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swapped = True
#
#         if swapped == False:
#             break
#         swapNumber += 1
#         print(swapNumber)
#     return swapNumber
#
# bubbleSort(lst)
#
# print("Sorted :")
# for i in range(len(lst)):
#     print("%d" % lst[i], end=" ")


# Lukas
# lst = [5, 1, 4, 2, 8]
#
#
# def bubble_sort(list_to_sort: list):
#     swap = True
#     while swap:
#         swap = False
#         for index in range(len(list_to_sort) - 1):
#             if list_to_sort[index + 1] < list_to_sort[index]:
#                 # temp = list_to_sort[index + 1]
#                 # list_to_sort[index + 1] = list_to_sort[index]
#                 # list_to_sort[index] = temp
#                 list_to_sort[index + 1], list_to_sort[index] = list_to_sort[index], list_to_sort[index + 1]
#                 swap = True
#
#
# print(lst)
# bubble_sort(lst)
# print(lst)

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above

