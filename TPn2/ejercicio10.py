#Realizar la carga del precio de un producto y la cantidad a llevar. 
#Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto).
precioProducto=int(input("Ingrese el precio del Producto: "))
cantidadProducto=int(input("Ingrese la cantidad del Producto: "))
print("Debe pagar por ",cantidadProducto," unidades de producto un total de: ",precioProducto*cantidadProducto)