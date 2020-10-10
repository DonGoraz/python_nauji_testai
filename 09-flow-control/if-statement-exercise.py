
numberis = input("Įveskite skaičių nuo 1 iki 7: ")

if numberis < "1":
    print("Nėra neigiamo dienų skaičiaus")
elif numberis == "1":
    print("Jūs pasirinkote Pirmadienį")
elif numberis == "2":
    print("Jūs pasirinkote Antradienį")
elif numberis == "3":
    print("Jūs pasirinkote Trečiadienį")
elif numberis == "4":
    print("Jūs pasirinkote Ketvirtadienį")
elif numberis == "5":
    print("Jūs pasirinkote Penktadienį")
elif numberis == "6":
    print("Jūs pasirinkote Šeštadienį")
elif numberis == "7":
    print("Jūs pasirinkote Sekmadienį")
else:
    print("Savaitė turi tik 7 dienas :)")