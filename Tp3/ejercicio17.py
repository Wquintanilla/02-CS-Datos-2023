'''Realizar un programa que solicite la carga por teclado de dos números, 
si el primero es mayor al segundo informar su suma y diferencia,
 en caso contrario informar el producto y la división del primero respecto al segundo.'''
num1=float(input("Ingrese el 1er numero: "))
num2=float(input("Ingrese el 2do numero: "))
if num1>num2:
    print("SUMA: ",num1+num2)
    print("RESTA: ",num1-num2)
else:
    print("PRODUCTO: ",num1*num2)
    print("DIVISION: ",num1/num2)