
import time


def calc_running_time(func, arg):
    t1 = time.time()

    func(arg)

    running_time = time.time() - t1
    return running_time


# # lst = [1,8,9,6,8]
# lst = list(range(100))
#
# count = 0
# for i in lst:
#     count += i
#     print(i)
#

"""
listo ilgis  - n

atliekamu operaciju skaicius - 3 * n

O(3*n) ~ O(n)

O(3*n^2 + 100*n + 10000) ~ O(n^2)

1. Odd or Even number,
2. Look-up table (dict) (Marius)
3. Find all possible pizza combinations  [desra, suris, grybai, jalapenai, majonezas, silke, burokas, ...] -> len(lst) = n
4. Find all permutations of a given set/string
5. Finding element on sorted list with binary search (Marius)
6. Find max element in unsorted list
7. 3 variables equation solver
8. Duplicate elements in list **(naïve)**
9. Duplicate elements in list using dict

"""




# def find_element_with_binary_search5(lst, elm):
#     k = 0
#     d = len(lst) - 1
#     while k <= d:
#         vid = k + (d - k) // 2;
#         if lst[vid] == elm:
#             return vid
#         elif lst[vid] < elm:
#             k = vid + 1
#         else:
#             d = vid - 1
#
#
# lst = list(range(10, 100000, 1))
#
# print(find_element_with_binary_search5(lst, 15))


# def look_up_table_dict2(lst, elm):
#     # list_to_dict = dict.fromkeys(lst, elm)
#     list_to_dict = {i: lst[i] for i in range(0, len(lst))}
#     print(f"ieškomas elementas {elm}")
#     print(list_to_dict)
#     for key, value in list_to_dict.items():
#         if value == elm:
#             print(f"ieškomo elemento {elm} raktas yra {key}")


def look_up_table_dict_2(lst, elm=5):
    # list_to_dict = dict.fromkeys(lst, elm)
    list_to_dict = {i: lst[i] for i in range(0, len(lst))}
    res = list_to_dict[elm]
    return res

#
# lst = list(range(10, 20, 1))
#
# look_up_table_dict2(lst, 19)

# def all_possible_pizaa_combination3(lst):
#     n = len(lst)
#     print(lst)
#     # list_to_dict = dict.fromkeys(lst,0)
#     # print(list_to_dict)
#     for i in lst:
#         print(i)
#         # newdict = dict(value='as', aab="ab", aac="ac")
#         # print(f"{key}; jo reiksme {value}")
#         # print(newdict)
#
#
#
#     print(list_to_dict)
#
#
# lst = list(range(1, 7, 1))
# all_possible_pizaa_combination3(lst)


input_sizes = [10, 100, 500, 1000, 10000, 50000, 100000, 1000000, 10000000]

running_times = []
for inp_zise in input_sizes:
    print(inp_zise)
    lst = list(range(inp_zise))
    rt = calc_running_time(look_up_table_dict_2, lst)
    running_times.append(rt)

for i in range(len(input_sizes)):
    print(f"input size: {input_sizes[i]}; running time: {running_times[i]}")