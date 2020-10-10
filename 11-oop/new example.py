from dataclasses import dataclass

@dataclass()
class Wheels():

    def kvieciams_metodas(self):
        print("pakviete paveldeta metoda")

    def kvieciamas_dar_vienas_metodas(self):
        print("pakviete kita metoda")


@dataclass()
class Car(Wheels):

    # def __init__(self):
    wheels = 4
    doors = 4

    def kviecia_kita_klase(self):
        self.kvieciams_metodas()

    def kvieciamas_dar_vienas_metodas(self):
        print("pakviete perrasyta  metoda")

    def padidink_ratu_skaiciu(self):
        self.wheels = self.wheels + 1
        print(self.wheels)

    def sumazink_ratu_skaiciu(self, *args, **kwargs):
        self.wheels = args[0]
        self.doors = kwargs['durys']
        print(self.wheels)
        print(self.doors)
        print(kwargs)
        print(args)

masina = Car()

masina.padidink_ratu_skaiciu()

#masina.sumazink_ratu_skaiciu(ratai = 3, durys = 7)

masina.sumazink_ratu_skaiciu(3,7, 9,2,5, ratai = 11, durys = 20)

masina.kviecia_kita_klase()

masina.kvieciamas_dar_vienas_metodas()