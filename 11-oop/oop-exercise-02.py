# Using @property decorator
class Celsius:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return round((self._temperature * 1.8) + 32, 2) # pries paskaiciuodamas jis daro getter ir tada tik perskaiciuoja

    #@property #getter
    def temperature1(self):
        print("Called fnc getter...")
        return self._temperature

    #@temperature.setter
    def temperature2(self, value):
        print("Called fnc setter...")
        if value < -273.15:
            print(f"Temperature below -273 is not possible {value}")
        self._temperature = value

    temperature = property(temperature1(self, value),temperature2(self, value))
# create an object

tmp = 37
while True : #amzinas ciklas kol nesustabdysim
   tmp = int(input("Enter Temperature: ")) # ivedam temperatura

   if tmp == 0: break #jeigu temperatura 0 sustabdom programa

   human = Celsius(tmp) # sukuriam objekta human (suveikia __init__) ir priskiriam jam temperatura suvesta consolej t.y. suveikia setter
   human_tmp_C = human.temperature # metodas getter t.y. @property gauna reiksme ir grazina ja priskyrimui
   print("temperatura C yra " + str(human_tmp_C)) # spaudinam kintamaji
   human_tmp_F = human.to_fahrenheit() # va cia idomiai kvieciam funkcija konvertavimo i fnc, bet ji pati kviecia getter nes jai reikia reiksmes
   print(f"temperatura F yra {str(human_tmp_F)}\n") # spausdinam kintamaji 37

print("Pabaiga")