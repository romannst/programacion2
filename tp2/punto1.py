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
    palindromo = True
    i = 0
    while len(cadena) != i and palindromo:
        if cadena_str.pop() != cadena[i]:
            palindromo = False
        i += 1
    if palindromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
esPalindromo(input("Ingrese otra cadena: ").upper())
