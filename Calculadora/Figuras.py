<<<<<<< HEAD
#Libreria
import math
#Area cuadrado
def area_cuadrado(lado):
    """
    Calcula el area del cuadrado
    a = l * l
    tipo float
    """
    area = lado * lado
    return area

#Area triangulo
def area_triangulo(base,altura):
    """
    Calcula el area del triangulo
    a = (b*h)/2
    tipo float
    """
    area = (base * altura)/2
    return area

#Area circulo
def area_circulo(radio):
    """
    Calcula el area del circulo
    a = pi.r^2
    tipo float
    """
    area = math.pi * radio * radio
=======
#Libreria
import math
#Area cuadrado
def area_cuadrado(lado):
    """
    Calcula el area del cuadrado
    a = l * l
    tipo float
    """
    area = lado * lado
    return area

#Area triangulo
def area_triangulo(base,altura):
    """
    Calcula el area del triangulo
    a = (b*h)/2
    tipo float
    """
    area = (base * altura)/2
    return area

#Area circulo
def area_circulo(radio):
    """
    Calcula el area del circulo
    a = pi.r^2
    tipo float
    """
    area = math.pi * radio * radio
>>>>>>> 0f3b15b052c297c2e0afdd043ee8040750f75275
    return area