#Variables
num1 = 2
num2 = 5
#OL
#AND
print(num1 == num2 and num1 <= num2) # 1 1 - V
print(num1 == num2 and num1 > num2) # 1 0 - F
print(num1 < num2 and num1 > num2) # 0 0 - F
print(num1 < num2 and num1 >= num2) # 0 1 - F

#Ejemplo1
#usuario = input("Digite el usuario: ")
#contraseña = input("Digite la contraseña: ")
#AND
#print(usuario == "jdgarcia3" and contraseña == "ftugy46!") # 1 1 - V

#OR
print(num1 == num2 or num1 <= num2) # 0 1 - V
print(num1 <= num2 or num1 > num2) # 1 0 - V
print(num1 > num2 or num1 > num2) # 0 0 - F
print(num1 > num2 or num1 <= num2) # 0 1 - F

#NOT
print(not True ) #F
print(not False ) #V