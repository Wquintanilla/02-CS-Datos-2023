'''Se pide confeccionar un programa que ingrese los dos datos por teclado 
e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido,
 y sabiendo que:
• Nivel máximo: Porcentaje>=90%.
• Nivel medio: Porcentaje>=75% y <90%.
• Nivel regular: Porcentaje>=50% y <75%.
• Fuera de nivel:Porcentaje<50%.'''
num1=float(input("Ingrese la CANTIDAD DE PREGUNTAS: "))
num2=float(input("Ingrese la RESPUESTAS CORRECTAS: "))
porcentaje=num2/num1
if porcentaje>=0.9:
    print("Nivel MAXIMO")
elif(porcentaje>=0.75):
    print("Nivel MEDIO")
elif(porcentaje>=0.50):
    print("Nivel REGULAR")
else:
    print("FUERA DE NIVEL")