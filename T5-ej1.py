#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# otra función que calcule el área de un círculo recibiendo el radio del mismo.

base = float(input("base = "))
altura = float(input("altura = "))
triangulo = (base*altura)/2
print(triangulo)

import math
pi = math.pi
radio = float(input("radio = "))
circulo = round(pi*radio**2,2)
print(circulo)