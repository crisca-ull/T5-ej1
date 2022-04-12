#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math
pi = math.pi

def area_triangulo(altura, base):
    print ((altura*base)/2)


def area_circulo(radio):
    print (round(pi,2)*(radio**2))

area_triangulo(3,4)
area_circulo(4)

