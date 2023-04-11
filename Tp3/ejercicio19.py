'''Se ingresa por teclado un número entero positivo de uno o dos dígitos (1..99) 
mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)'''
num=int(input("INGRESE UN NUMERO entero positivo de una o 2 cifras:  "))
contadorCifra=0
aux=num
while aux>0:
    contadorCifra+=1
    aux=int(aux/10)
print("el numero tiene ",contadorCifra," Cifras")