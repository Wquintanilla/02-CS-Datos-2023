print("PAGO DE Impuestos Personales de Ingresos")
print(("*"*50),"\n")
ingCiudadano=float(input("Coloque valor de ingreso del ciudadano\n"))
if ingCiudadano<85528:
    impuesto=(ingCiudadano*0.18)-556.02
else:
    impuesto=14839.02+(ingCiudadano-85528)*0.32

if impuesto < 0:
    impuesto=0.
print("-"*40,"\n" )
print("El usuario con un ingreso de:",ingCiudadano,"$ ")
print("debe abonar un impuesto de: ",round(impuesto,2),"$",)
