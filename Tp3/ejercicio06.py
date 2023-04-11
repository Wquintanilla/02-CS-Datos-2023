#Agregar un print con un mensaje con diseño

secret_number=777
numIgresado=int(input("Ingrese un numero entero y adivine el numero: "))
while secret_number!=numIgresado:
    
    print("¡Ja,ja!¡Estas atrapado en mi bucle!")
    numIgresado=int(input("ingrese nuevamente un numero entero: "))
print("\n"*10,"El numero es ",numIgresado,"\n¡Bien echo!¡eres libre!")