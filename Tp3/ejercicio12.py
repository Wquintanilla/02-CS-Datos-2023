'''Crea un programa con un bucle for y una sentencia continue.
El programa debe iterar sobre una cadena de dígitos, 
reemplazar cada 0 con x, 
e imprimir la cadena modificada en la pantalla.'''


cadenaDigitos="123503565022002025200023230"
for i in range(len(cadenaDigitos)) :
    if cadenaDigitos[i] == "0":
        print("X",end="")
        continue
    print(cadenaDigitos[i],end="")
