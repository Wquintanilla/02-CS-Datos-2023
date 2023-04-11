'''Se cargan por teclado tres números distintos.
 Mostrar por pantalla el mayor de ellos.'''
num1=float(input("Ingrese el numero N° 1 :  "))

for i in range(1,3):
    print("Ingrese el numero N°",i+1,": ",end="")
    nota=float(input(""))
    if num1<nota:
       num1=nota
print("El numero de mas grande es: ",num1)