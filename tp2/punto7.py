ruta = r"C:\Users\roman\programacion2\tp2\productos.txt"
archivo = open(ruta, "r")
diccionario_productos = {
    'codigo': [],
    'nombre': [],
    'precio': []
}
for linea in archivo:
    codigo, nombre, precio = linea.strip().split(";")
    diccionario_productos['codigo'].append(int(codigo))
    diccionario_productos['nombre'].append(nombre)
    diccionario_productos['precio'].append(int(precio))
archivo.close()

nombre_producto = input("Ingrese el nombre del producto a buscar: ").lower()
if nombre_producto in diccionario_productos['nombre']:
    indice = diccionario_productos['nombre'].index(nombre_producto)
    codigo = diccionario_productos['codigo'][indice]
    precio = diccionario_productos['precio'][indice]
    print(f"El producto {nombre_producto} con código {codigo} vale ${precio}.")
else:
    print(f"El producto {nombre_producto} no se encuentra registrado en el almacen.")