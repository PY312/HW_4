from Calculators import division
from Calculators import multiplication
from Calculators import summation
from Calculators import subtraction

class Calculator():
    def summa(a,b):
        print (summation.Summation.summa(a, b))

    def devis (a,b):
        print(division.Divisions.divis(a,b))

    def multiplicat (a,b):
        print (multiplication.Multiplication.multiplicat(a,b))

    def substract (a,b):
        print (subtraction.Subtraction.subtract(a,b))


# print (division.Divisions.divis(10, 2))
# print (multiplication.Multiplication.multiplicat(10, 2))
# print (summation.Summation.summa(10, 2, 3, 20, 17))
# print (subtraction.Subtraction.subtract(10, 2))