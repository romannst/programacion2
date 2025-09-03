ruta = r"C:\Users\roman\programacion2\tp2\distancias.txt"
archivo = open(ruta, "r")
suma = 0
contador = 0
distancias = []
for linea in archivo:
    distancia = int(linea.strip())  # strip() para eliminar saltos de línea
    suma += distancia
    contador += 1
    distancias.append(distancia) 
archivo.close()

promedio = suma / contador if contador > 0 else 0
dis_mayores_prom = []
for distancia in distancias:
    if distancia > promedio:
        dis_mayores_prom.append(distancia)
        
print(f"La distancia promedio es {promedio:.2f}")
print(f"Las distancias mayores a la promedio son: {dis_mayores_prom}")