#variable
opcion = 0
#Estructura repeticion
while opcion != 6:
    #Menu calculadora
    print("\nHola Calculadora" )
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Division")
    print("5. Potencia")
    print("6. Salir")
    #opcion a ingresar
    try:
        opcion = int(input("Digite la opcion de la calculadora: "))
        if opcion == 1:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1 + num2
            print(f"Suma = {resultado}")
        elif opcion == 2:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1 - num2
            print(f"Resta = {resultado}")
        elif opcion == 3:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1 * num2
            print(f"Multiplicación = {resultado}")
        elif opcion == 4:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1 / num2
            print(f"Division = {resultado}")    
        elif opcion == 5:
            base = int(input("Digite el primer numero: "))
            potencia = int(input("Digite el segundo numero: "))
            resultado = base ** potencia
            print(f"Potencia = {resultado}")
        elif opcion == 6:
            print(f"Saliendo de la calculadora...")
        else:
            print("Error")
    except ValueError:
        print("Ingrese una opcion valida")            
print("Gracias por utilizar la calculadora")      

