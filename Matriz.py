#Declarar una matriz
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Sintaxis 2
matriz2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

#Recorrer matriz
for filas in matriz1:
    for elementos in filas:
        print(f"Elementos matriz: {elementos}")

#Tamaños matriz
f = len(matriz1)
print(f"Tamaño filas: {f}")
c = len(matriz1[2])
print(f"Tamaño columnas: {c}")

#Recorrer matriz con range
for i in range(f):
    for j in range(c):
        print(f"Posición {i},{j}: {matriz1[i][j]}")

print(matriz1[1][2])