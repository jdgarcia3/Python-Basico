"""
POO - Creación de una clase
Clase persona
Atributos
*   Nombre
*   Edad
Metodos
*   saludar()
"""
#Crear clase persona
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
  
  def cumplir_anios(self):
    self.edad += 1

#Llamar clase persona
persona1 = Persona("Juan", 25)
persona1.saludar()
persona1.cumplir_anios()
persona1.saludar()

#Clase vehiculo con 10 atributos y 10 metodos
class vehiculo:
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.velocidad = 0
  
  def acelerar(self, incremento):
    self.velocidad += incremento

  def frenar(self, decremento):
    self.velocidad -= decremento

#Lamar clase vehiculo
carro1 = vehiculo("Toyota", "Corolla", "Rojo")
carro1.acelerar(30)
print(carro1.velocidad)
carro1.frenar(10)
print(carro1.velocidad)