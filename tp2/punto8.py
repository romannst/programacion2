# ruta = r"C:\Users\roman\programacion2\tp2\productos.txt"
ruta_2 = r"C:\Users\roman\programacion2\tp2\stock.txt"
# archivo_productos = open(ruta, "r")
archivo_stock = open(ruta_2, "r")
ruta_3 = r"C:\Users\roman\programacion2\tp2\compras.txt"
archivo_compras = open(ruta_3, "w")

for linea in archivo_stock:
    codigo_producto, stock_minimo, stock_real = linea.strip().split(";")
    stock_real = int(stock_real)
    stock_minimo = int(stock_minimo)
    if stock_real < stock_minimo:
        archivo_compras.write(f"Código del producto: {codigo_producto}; Cantidad a comprar: {stock_minimo-stock_real}\n")
archivo_stock.close()
archivo_compras.close()

archivo_compras = open(ruta_3, "r")
for linea in archivo_compras:
    print(linea)
archivo_compras.close()