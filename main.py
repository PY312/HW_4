from Calculators import Calculator as calc
print (calc.division.Divisions.divis(10, 2))
import random

rand_list = []
while len(rand_list) < 20:
    i = random.randint(1, 100)
    if i not in rand_list:
        rand_list.append(i)


a = random.choice(rand_list)
b = random.choice(rand_list)

print('список', rand_list)
print('первое число', a)
print('второе число', b)


calc.Calculator.summa(a, b)
calc.Calculator.multiplicat(a, b)
calc.Calculator.devis(a, b)
calc.Calculator.substract(a, b)
