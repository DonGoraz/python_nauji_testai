class Darbuotuojas:
    def __init__(self, name, surename):
        self._name = ''
        self.name = name
        self.surename = surename
    @property
    def fullname(self):
        return f'{self.name} {self.surename}'
    @property
    def email(self):
        return f'{self.name.lower()}.{self.surename.lower()}@filrma.lt'
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value_to_set):
        if len(value_to_set) >= 3:
            self._name = value_to_set
        else:
            print(f"Per trumpas vardas {value_to_set}")

class DarbuotuojasNuskaitytuvas:
    def __init__(self, kelias_iki_failo):
        self.file_path = kelias_iki_failo
    def execute(self):
        darbuotouju_sarasas = []
        with open(self.file_path) as f: # f is a file object
            for i, line in enumerate(f): # iterate every line of the file
                if i == 0: # skip first line
                    continue
                clean_line = line.rstrip() # remove "\n" - end of line character at the end of each line
                if clean_line == "": # skip empty lines
                    continue
                print(clean_line)
                darbuotuojas_values = clean_line.split(',')
                darbuotuojas_values = [reiksme.strip() for reiksme in darbuotuojas_values]
                print("-" * 40)
                print(darbuotuojas_values)
                darbuotojas = Darbuotuojas(*darbuotuojas_values[:2])
                darbuotouju_sarasas.append(darbuotojas)
        return darbuotouju_sarasas
    @property
    def darbuotoujai(self):
        return self.execute()
nuskaitytuvas = DarbuotuojasNuskaitytuvas('darbuotojai.txt')
print(nuskaitytuvas.darbuotoujai)
for darbuotuojas in nuskaitytuvas.darbuotoujai:
    print(darbuotuojas.fullname)
    print(darbuotuojas.email)