#Funcion menu principal
def menu ():
    """
    Muestra el menu de las figuras geometricas,
    retor la variable opcion
    """
    print("\n Bienvenido a la cálculadora de figuras")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Salir")
    op = int(input("Digite una opción del menú: "))
    return op

#Mostrar informacion selecionada
def opcion_seleccionada(op):
    """
    Mostrar lo seleccionado del menu
    """
    #Variables
    CUDRADO = 1
    TRIANGULO = 2
    CIRCULO = 3
    SALIR = 4
    #Condicionales
    if op == 1:
        print(f"Usted selecciono la opción CUADRADO")
        return CUDRADO
    elif op == 2:
        print(f"Usted selecciono la opción TRIANGULO")
        return TRIANGULO
    elif op == 3:
        print(f"Usted selecciono la opción CIRCULO")
        return CIRCULO
    elif op == 4:
        print(f"Saliendo de la calculadora....")
        return SALIR
    else:
        print(f"Opcion no valida!!!")
        return "Opcion no valida!!!"

#Solicitud de informacion
#Cuadrado
def solicitud_cuadrado ():
    """
    Solicita el lado para calculo de area
    lado, tipo de dato float
    """
    lado = float(input("Digite el lado: "))
    return lado

#Triangulo
def solicitud_triangulo ():
    """
    Solicita base y altura para calculo de area
    base y altura, tipo de dato float, retorna primero
    la base y despues la altura
    """
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base,altura

#Circulo
def solicitud_circulo ():
    """
    Solicita el radio para calculo de area
    , tipo de dato float
    """
    radio = float(input("Digite el radio: "))
    return radio