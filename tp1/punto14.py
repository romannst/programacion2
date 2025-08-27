texto = input("Ingrese una cadena de texto: ")
cant_vocales = 0
for caracter in texto:
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        cant_vocales += 1
print("Cantidad de vocales:", cant_vocales)