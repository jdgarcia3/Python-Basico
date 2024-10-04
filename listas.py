#Crear una lista
lista = [90,"a","viernes",False,4.5]
print(f"Los datos de la lista son: {lista}")
#Datos en una lista
print(lista[2])
print(lista[4])
print(lista[-4])
print(lista[-3])
#Recorrer un lista
print(lista[1:4])
print(lista[0:3])
print(lista[-1:])
#Agregar datos a una lista
numeros = [1,5]
numeros.append(100)
numeros.append("jgarcia3@unisangil.edu.co")
print(numeros)
#Tamaño lista
longitud = numeros.__len__()
print(f"El tamaño de la lista es {longitud}")
#insert
numeros.insert(2,"David")
print(numeros)
numeros.insert(1,"D")
print(numeros)
#Reemplazar datos de una lista
numeros[-1] = "jdgarcia@gmail.com"
print(numeros)
#Eliminar datos lista
numeros.remove(100)
print(numeros)
numeros.pop()
print(numeros)
numeros[2:4] = []
print(numeros)
#Recorre lista
for i in lista:
    print(f"Dato lista: {i}")
#Invertir datos de una lista
lista.reverse()
print(lista)
#Ordenar datos de una lista
lista_2 =[10,2,4,5,7,8,3]
print(sorted(lista_2))
lista_2.sort(reverse=True)
print(lista_2)
