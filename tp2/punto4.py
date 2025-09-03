numero = input("Ingrese un número: ")
corte = False
while not corte:
    try:
        numero = int(numero)
        corte = True
    except ValueError:
        print("Error: No se ingresó un número.")
        numero = input("Ingrese un número: ")

lista_digitos = []
while numero != 0:
    digito = numero % 10
    lista_digitos.append(digito)
    numero //= 10

# digito_mayor = max(lista_digitos)
digito_mayor = -1
for digito in lista_digitos:
    if digito > digito_mayor:
        digito_mayor = digito
print(f"El dígito mayor es: {digito_mayor}")