'''Se ingresan tres notas de un alumno, 
si el promedio es mayor o igual a siete 
mostrar un mensaje "Promocionado".'''
nota=0
for i in range(3):
    print("Ingrese la nota N°",i+1," del ALUMNO :",end="")
    nota+=float(input(""))
if nota/i>=7:
    print("Promocionado")
else:
    print("NO Promosiona")