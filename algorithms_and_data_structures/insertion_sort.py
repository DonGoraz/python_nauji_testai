import random

# lst = [random.randint(0, 10) for i in range(20)]
lst = [9,9,8,7,6,5,4,3,2,1,0]

# Marius (kreivas)
print(lst)
insertion_count = 0
pass_count = 0
cycle_count = 0
for key, value in enumerate(lst):
    # print("------------------------------nauja iteracija", key, value)
    # print('cia mano reiksme', key, value)
    k = 0
    for i in range(0, key):
        k = i + 1
        # print('cia mano k', k)
        # print('cia mano key', key)
        sena_reiksme = lst[key - k]
        # print("sena_reiksme key-k", [key - k], sena_reiksme)
        nauja_reiksme = lst[key - i]
        # print("nauja_reiksme key - i", [key - i], nauja_reiksme)
        # print(f"=========lyginame {nauja_reiksme} < {sena_reiksme}")
        if nauja_reiksme < sena_reiksme:
            # print(f"+++++++++lyginame {nauja_reiksme} < {sena_reiksme}")
            lst[key - k] = nauja_reiksme
            lst[key - i] = sena_reiksme
            print(f"{lst}")
            cycle_count += 1

        insertion_count += 1

    pass_count += 1

print('='*100)
print(lst)
print(f'[Insertion sort] Marius: pass_count={pass_count}; insertion_count={insertion_count}; cycle_count={cycle_count}')
print('='*100)
print()


# mantas (geras)
# lst = [9,9,8,7,6,5,4,3,2,1,0]
# def InsertionSort(lst):
#     swapNumber = 0
#     pass_count = 0
#
#     for i in range(1, len(lst)):
#         swap = lst[i]
#         j = i - 1
#
#         while j >= 0 and swap < lst[j]:
#             lst[j+1] = lst[j]
#             j -= 1
#             print(lst)
#         lst[j + 1] = swap
#
#
#     return swapNumber, pass_count, lst
#
#
# InsertionSort(lst)

# Gedas (blogas)
# print(lst)
# sorted_lst = []
# sorted_lst.insert(0,lst[0])
# for i in range(1,len(lst)):
#     print(lst)
#     for j in range(0, len(sorted_lst)):
#         print(sorted_lst)
#         if lst[i] <= sorted_lst[j] and j==0:
#             sorted_lst.insert(j,lst[i])
#             break
#         elif lst[i] <= sorted_lst[j] and lst[i] >= sorted_lst[j]:
#             sorted_lst.insert(j+1, lst[i])
#             break
#         elif lst[i] > sorted_lst[len(sorted_lst)-j-1]:
#             sorted_lst.insert(len(sorted_lst)-j,lst[i])
#             break
#
# print(sorted_lst)
#
# # Dovydas (blogas)
# lst = [4, 9, 2, 10, 12, 1, 5, 6]
# sorted_lst = list()
#
# sorted_lst.append(lst[0])
# for i in range(1, len(lst)):
#     for j in range(len(sorted_lst) - 1, -1, -1):
#         print(sorted_lst)
#         if lst[i] < sorted_lst[j]:
#             continue
#         elif lst[i] > sorted_lst[j]:
#             j += 1
#             break
#
#     sorted_lst.insert(j, lst[i])
#
#
# print(sorted_lst)
#
# # Andrius (kreivas)
# for i in range(len(lst)):
#     for j in range(len(lst[0:i+1])):
#         if lst[i] < lst[j]:
#             lst[j], lst[i] = lst[i], lst[j]
#             print(lst)
#
#
# # Irmantas (geras)
# lst = [9, 3, 9, 5, 4, 1, 5, 2, 5, 6, 7]
# l = len(lst)
# for i in range(0, (l-1)):
#     if lst[i] > lst[i + 1]:
#         for j in range((i+1), 0, -1):
#             while lst[j]<lst[j-1]:
#                 lst[j-1],lst[j] = lst[j],lst[j-1]
#                 print(lst)






