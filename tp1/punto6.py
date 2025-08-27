num = input("Ingrese un numero entero positivo: ")
try:
    num = int(num)
    if num <= 0:
        print("Por favor, ingrese un número entero positivo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
for i in range(1, num + 1):
    print(i, end=" ")