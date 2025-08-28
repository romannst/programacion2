cant_notas = input("Ingrese la cantidad de notas que desea cargar: ")
try:
    cant_notas = int(cant_notas)
except:
    print("Entrada inválida. Por favor, ingrese un número entero.")
    exit()
lista_notas = [nota for nota in [input(f"Ingrese la nota {i+1}: ") for i in range(cant_notas)]]
nota_mas_alta = max(lista_notas)
indice_mas_alta = lista_notas.index(nota_mas_alta)
print(f"La nota más alta es {nota_mas_alta} en el índice {indice_mas_alta} del arreglo")