import sys
print(f"Ivestis: {sys.argv}")
if len(sys.argv) == 4:
    countries = {}
    country, capital = sys.argv[1].split(",")
    countries[country] = capital
    country, capital = sys.argv[2].split(",")
    countries[country] = capital
    country, capital = sys.argv[3].split(",")
    countries[country] = capital
    print(f"COUNTRIES: {countries}")
else:
    print("Bloga ivestis")