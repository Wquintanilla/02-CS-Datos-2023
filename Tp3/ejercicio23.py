'''Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
 y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
   Mostrar un mensaje de error si el número de cifras es mayor'''
num=int(input("INGRESE UN NUMERO entero positivo de hasta 3 cifras:  "))
contadorCifra=0
aux=num
while aux>0:
    contadorCifra+=1
    aux=int(aux/10)
if contadorCifra<4:
    print("el numero tiene ",contadorCifra," Cifras")
else:
    print("ERROR INGRESO UN NUMERO MAYOR A 3 cifras")