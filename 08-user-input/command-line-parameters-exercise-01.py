import sys

# print(f"%vestis: {sys.argv}")
# #print(sys.argv)
# if len(sys.argv) == 3:
#     country = sys.argv[1]
#     capital = sys.argv[2]
#
#     print(f"{country} -> {capital}")
# else:
#     print("Bloga ivestis")


dictionary_list = dict()


if len(sys.argv) == 7:
    i = 1
    while i < 6:
        country = sys.argv[i]
        i += 1
        capital = sys.argv[i]
        i += 1
        dictionary_list[country] = capital
    print(f"List, {dictionary_list}")
else:
    print("Bloga ivestis")


