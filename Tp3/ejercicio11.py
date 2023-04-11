'''Crea un programa con un bucle for y una sentencia break. 
El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.'''
correo="wquintanilla@bue.edu.ar"
correo=input("Ingrese el correo electronico")
salida=""

for i in range(len(correo)):
    if correo[i]=="@":
        break
    print(correo[i],end="")

    salida=salida+correo[i]
print("")

