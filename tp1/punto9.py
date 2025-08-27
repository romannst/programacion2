A = input("Ingrese un numero entero positivo: ")
B = input("Ingrese un numero entero positivo: ")
X = input("Ingrese un numero entero positivo: ")
try:
    A = int(A)
    B = int(B)
    X = int(X)
    if A <= 0 or B <= 0 or X <= 0:
        print("Por favor, ingrese números enteros positivos.")
except ValueError:
    print("Por favor, ingrese números enteros válidos.")
for n in range(A, B + 1):
    if n % X == 0:
        print(n, end=" ")