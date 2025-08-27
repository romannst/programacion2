cond = True
lista = list()
while cond:
    try:
        num = int(input("Ingrese un número entero positivo (0 para salir): "))
        if num == 0:
            cond = False
        else:
            lista.append(num)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero positivo.")
if lista == sorted(lista):
    print("La secuencia estaba ordenada de menor a mayor.")
else:
    print("La secuencia no estaba ordenada de menor a mayor.")
