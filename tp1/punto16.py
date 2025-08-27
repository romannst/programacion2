texto = input("Ingrese un texto: ")
lista_texto = texto.split()
cant_mas_larga = 0
palabra_mas_larga = ""
for palabra in lista_texto:
    aux_cant = len(palabra)
    if aux_cant > cant_mas_larga:
        cant_mas_larga = aux_cant
        palabra_mas_larga = palabra
print(f"La palabra más larga es {palabra_mas_larga} con {cant_mas_larga} letras.")
