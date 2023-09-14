class Calculator:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return self.num1 + other

    def __sub__(self, other):
        return self.num1 - other

    def __mul__(self, other):
        return self.num1 * other

    def __div__(self, other):
        return self.num1 - other

