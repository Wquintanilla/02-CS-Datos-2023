'''Realizar un programa que solicite ingresar dos números distintos
 y muestre por pantalla el mayor de ellos.'''

num1=float(input("Ingrese el 1er numero: "))
num2=float(input("Ingrese el 2do numero: "))
print("\nEl numero mayor es ",end="")
if num1>num2:
    print(num1)
else:
    print(num2)
