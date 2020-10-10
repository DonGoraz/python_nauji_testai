print("Welcome to the interactive greeting system.")

dictionary_list = dict()

for i in range(3):
    # user_country = input("Enter your Country, Capital: ")
    # x = user_country.split(", ")
    # dictionary_list[x[0]] = x[1]
    country, capital = input("Enter your Country, Capital: ").split(", ")
    dictionary_list[country] = capital


print(f"List, {dictionary_list}")