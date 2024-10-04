#Estructura de repetición FOR
for i in range(2):#comienza desde 0
    print(f"Su dato es {i}")

#Estructura de repetición FOR
for i in range(20,101):#comienza inicio,fin -1
    print(f"Su dato es {i}")

#Estructura de repetición FOR
for i in range(1,10,2):#comienza inicio,fin-1,incremento
    print(f"Su dato es {i}")

#Estructura de repetición FOR
for letra in "Python":
    print(letra)

#Ejemplo 1
cadena = "Python"
for letra in cadena:
    if letra == "h":
        print("Se encontrol una h")
        break
    else:
        print("Letra no encontrada")
print("Esta por fuera del ciclo for")