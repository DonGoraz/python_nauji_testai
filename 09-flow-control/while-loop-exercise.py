
ivedimas = ""

while ivedimas != "exit":
    ivedimas = input("Įveskite: ")
    if ivedimas == "no-print":
        continue
    elif ivedimas == "exit-no-print":
        break
    else:
        print(f"{ivedimas}")

else:
    print("Done.")
