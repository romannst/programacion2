oracion = input("Ingrese una oración: ")
cant_caracteres = len(oracion)
cant_letras = 0
for i in oracion:
    if i.isalpha():
        cant_letras += 1
lista_palabras = oracion.split()
cant_separadas = len(lista_palabras)
print(f"Cantidad de caracteres: {cant_caracteres}")
print(f"Cantidad de letras: {cant_letras}")
print(f"Cantidad de palabras separadas: {cant_separadas}")