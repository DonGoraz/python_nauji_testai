print("Welcome to the interactive greeting system.")

dictionary_list = dict()
i = 0
while i < 3:
    user_country = input("Enter your Country: ")
    user_capital = input("Enter your Capital: ")
    dictionary_list = {user_country: user_capital}
    i += 1

print(f"List, {dictionary_list}")