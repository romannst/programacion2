cant_valores = input("Ingrese un numero entero positivo: ")
try:
    cant_valores = int(cant_valores)
    if cant_valores < 0:
        print("Por favor, ingrese un número entero positivo o cero.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
suma_valores = 0
promedio_valores = 0
aux_cant = cant_valores
while(aux_cant > 0):
    valor_ingresado = input("Ingrese un valor: ")
    try:
        valor_ingresado = float(valor_ingresado)
        suma_valores += valor_ingresado
        aux_cant -= 1
    except ValueError:
        print("Por favor, ingrese un número válido.")
if cant_valores > 0:
    promedio_valores = suma_valores / cant_valores
print(f"La suma de los valores es: {suma_valores:.2f}")
print(f"El promedio de los valores es: {promedio_valores:.2f}")