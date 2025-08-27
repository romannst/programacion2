lado_1 = int(input("Ingrese el lado 1: "))
lado_2 = int(input("Ingrese el lado 2: "))
lado_3 = int(input("Ingrese el lado 3: "))
if lado_1 == lado_2 == lado_3:
    print("El triángulo es equilátero")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
