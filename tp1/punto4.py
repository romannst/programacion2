num_1 = int(input("Ingrese el número 1: "))
num_2 = int(input("Ingrese el número 2: "))
num_3 = int(input("Ingrese el número 3: "))
if num_1 > num_2 and num_1 > num_3:
    print("El número 1 es el mayor.")
elif num_2 > num_1 and num_2 > num_3:
    print("El número 2 es el mayor.")
else:
    print("El número 3 es el mayor.")