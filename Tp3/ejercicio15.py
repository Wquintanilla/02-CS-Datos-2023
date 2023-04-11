'''Ingresar el sueldo de una persona, si supera los 3000 dolares 
mostrar un mensaje en pantalla indicando que debe abonar impuestos.'''
sueldo=float(input("Ingrese el sueldo en dolares: "))
if sueldo>3000:
    print("Debe pagar impuesto")
else:
    print("Sueldo es menor a 3000 dolares NO PAGA IMPUESTO")