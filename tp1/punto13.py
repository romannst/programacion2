car = input("Ingrese un caracter: ")
cond = False
while not cond:
    try:
        num_nat = int(input("Ingrese la cantidad de repeticiones (un n natural): "))
        if num_nat > 0:
            cond = True
        else:
            print("Por favor, ingrese un numero natural.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número natural.")
while num_nat != 0:
    print(car, end="")
    num_nat -= 1