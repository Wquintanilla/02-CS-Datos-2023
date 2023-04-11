'''Se ingresa por teclado un valor entero, 
mostrar una leyenda que indique si el número es positivo,
negativo o nulo (es decir cero)'''
num=int(input("Ingrese un numero entero: "))
if num>0:
    print("Positivo")
elif(num<0):
     print("Negativo")
else:
     print("Nulo")