class Animal:

    def __init__(self, animal, breed):
        self.animal = animal
        self.breed = breed

    def __repr__(self):  # called if disable __str__
        return "You just called __repr__"

    def __str__(self):
        return "You just called __str__"

aaa = Animal("Dog", "Doberman")
aaa
print(aaa)


