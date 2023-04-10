#Escribir un programa que lea un entero positivo,
#introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los primeros enteros positivos puede ser calculada de la siguiente forma
#suma=(n*(n+1))/2
num=int(input("Ingrese un entero positivo n: "))
print("la suma de todos los enteros desde 1 hasta ",num," es ",int((num*(num+1))/2))