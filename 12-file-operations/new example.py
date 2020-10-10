
listas = ["1","2","3"]
dictionary = {"name": "AP", "website": "url"}
with open("file.txt", 'w') as f:
    for k, v in dictionary.items():
        f.writelines(k)

# for i in listas:
#     f.writelines(i)
# print("kazkas")
