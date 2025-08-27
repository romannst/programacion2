def reverso(cadena):
    cadena_str = []
    for letra in cadena:
        cadena_str.append(letra)
    while len(cadena_str) != 0:
        print(cadena_str.pop(), end="")
reverso(input("Ingrese una cadena: "))
print()

def esPalindromo(cadena):
    cadena_str = []
    for letra in cadena:
        cadena_str.append(letra)
    es = True
    i = 0
    while len(cadena) != i and es:
        if(cadena_str.pop() != cadena[i]):
            es = False
        i += 1
    if es:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
esPalindromo(input("Ingrese otra cadena: ").upper())
