ruta_1 = r"C:\Users\roman\programacion2\tp2\alumnos.txt"
ruta_2 = r"C:\Users\roman\programacion2\tp2\id_alumnos.txt"

# Crear diccionario legajo -> apellido y nombre
diccionario_id = {}
with open(ruta_2, "r") as archivo_id_alumnos:
    for linea in archivo_id_alumnos:
        legajo, apellido, nombre = linea.strip().split(";")
        diccionario_id[legajo] = f"{apellido}, {nombre}"
with open(ruta_1, "r") as archivo_alumnos, open("Promocion.txt", "w") as archivo_promocion:
    for linea in archivo_alumnos:
        legajo_alumno, nota1, nota2, nota3 = linea.strip().split(";")
        promedio = (int(nota1) + int(nota2) + int(nota3)) / 3
        if promedio > 7:
            # Buscar apellido y nombre por legajo
            if legajo_alumno in diccionario_id:
                archivo_promocion.write(diccionario_id[legajo_alumno] + "\n")
                print(diccionario_id[legajo_alumno])  # Muestra en pantalla
