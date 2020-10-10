class Darbuotojas:
    class_variable = 1

    def __init__(self, name, surname):
        self.darbuotojas = ["Antanas", "Petras", "Jonas", "Vincas"]
        self._name = ''
        self.name = name
        #TODO prideti slapta varda kad nebutu rekursijos
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @property
    def email(self):
        return f'{self._name}{self.surname}@firma.lt'

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value_to_set):
        if value_to_set in self.darbuotojas:
        # if len(value_to_set) >= 3:
            self._name = value_to_set
        else:
            # print("per trumpas vardas")
            print(f'Toks {value_to_set} cia nedirba. Darbuotojai {self.darbuotojas}')

darbuotojas1 = Darbuotojas("Marius", "M")
print(darbuotojas1.fullname)
print(darbuotojas1.email)

#darbuotojas1.name = "Ro"
darbuotojas2 = Darbuotojas("Jonas", "M")
print(darbuotojas2.fullname)
print(darbuotojas2.email)