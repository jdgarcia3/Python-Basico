#Función
def mensaje():
    """
    mostrar mensaje programación 1:str
    """
    print("Programación 1")
    x=10

#Llamar función
mensaje()

#Crear función con parametros
def suma (num1,num2):
    """
    Genera la suma de dos numeros 
    enteros con variables de entrada 
    num1,num2
    """
    rta = num1 + num2
    print(f"la suma entre {num1} + {num2} = {rta}")

#LLamar funcion 
suma(1,2)

#Funcion pedir datos
def solicitar_datos():
    """
    solicita num1 y num2, transforma a tipo de dato
    entero y retorna la informacion
    """
    num1 = int(input("Digite el número 1: "))
    num2 = int(input("Digite el número 2: "))
    return num1,num2

#Llamar funcion 
a,b = solicitar_datos()
print(f"Numeros digitados {a} y {b}")
#LLamar a suma
suma(a,b)

#Funcion *
def multiplicacion (num1,num2):
    """
    * 2 numeros de tipo entero y los retorna
    """
    rta = num1 * num2
    return rta

rta = multiplicacion(a,b)
print(f"El resultado de la * = {rta}")

suma(rta,a)
