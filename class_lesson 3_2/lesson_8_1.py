from math import gcd # gcd - Наибольший общий делитель двух чисел
from random import randint

class My_Fraction:
    def __init__(self, num, den):
        if num != 0 and den != 0:
            k = gcd(num, den)       # находим НОД
            self.num = num // k     # числитель
            self.den = den // k     # знаменатель
        else:
            raise ValueError
        
    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        return My_Fraction(randint(num_min, num_max), randint(den_min, den_max))

    def __str__(self):              # метод преобразования дроби в строку
        return f'{self.num}/{self.den}'

    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num * other, self.den)
        return self
    
    def __truediv__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num * other, self.den)
        return TypeError


#-----------------------------------------------------
# список из случайных дробей
a = [My_Fraction.generate(1, 9, 1, 9) for i in range(5)]
for f in a:
    b = My_Fraction.generate(1, 9, 1, 9)        # дробь для правого операнда
    cm = f * b
    print(f'{f} * {b} = {cm}')                  # пример умножения на дробь
    cd = f / b
    print(f'{f} / {b} = {cd}')                  # пример деления на дробь
    n = randint(1, 9)                           # число для правого операнда
    cm = f * n
    print(f'{f} * {n} = {cm}')                  # пример  умножения на число
    cd = f / n
    print(f'{f} / {n} = {cd}')                  # пример деления на число