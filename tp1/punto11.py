num_entero = input("Ingrese un número entero (negativo para terminar): ")
try:
    num_entero = int(num_entero)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
promedio_nums = 0
suma_enteros = 0
cant_n = 0
while num_entero >= 0:
    suma_enteros += num_entero
    cant_n += 1
    num_entero = input("Ingrese un número entero (negativo para terminar): ")
    try:
        num_entero = int(num_entero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
if cant_n > 0:
    promedio_nums = suma_enteros / cant_n
    print(f"El promedio es {promedio_nums:.2f} con un total de {cant_n} ingresos.")
else:
    print("No se ingresaron números válidos.")