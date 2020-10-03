class Calculator:

    def add(self, a, b):
        try:
            z, x = float(a), float(b)
        except ValueError:
            print(f"bloga reikšmė {a} arba {b}")
            return 1 - 1

        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return pow(a, b)


# calc = Calculator(2,3)
# calc.add()
# calc.substract()
# calc.multiply()
# calc.divide()
# calc.power()
