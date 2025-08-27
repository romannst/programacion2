cadena = input("Ingrese una cadena de texto: ")
cant = 0
for c in cadena:
    if c == ' ':
        cant += 1
print(f"La cantidad de espacios en la cadena es: {cant}")