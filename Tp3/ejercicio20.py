'''Confeccionar un programa que pida por teclado tres notas de un alumno, 
calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado".'''
nota=0
for i in range(3):
    print("Ingrese la nota N°",i+1," del ALUMNO :",end="")
    nota+=float(input(""))
promedio=nota/(i+1)
print(promedio)
if promedio>=7:
    print("Promocionado")
elif(promedio>=4):
    print("REGULAR")
else:
    print("REPROBADO")
