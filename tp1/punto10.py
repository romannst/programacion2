largo = input("Ingrese el largo del rectángulo: ")
ancho = input("Ingrese el ancho del rectángulo: ")

try:
    largo = int(largo)
    ancho = int(ancho)
    if largo <= 0 or ancho <= 0:
        print("Por favor, ingrese valores positivos.")
    elif largo > 40 or ancho > 40:
        print("Las medidas no pueden ser mayores a 40.")
    elif largo == ancho:
        print("El rectángulo es un cuadrado.")
    else:
        for i in range(ancho):
            print("*" * largo)
except ValueError:
    print("Por favor, las medidas de los lados deben ser enteros.")

# # Programa para dibujar un rectángulo con caracteres
# # Función para verificar que la entrada es un entero y <= 40
# def pedir_lado(nombre):
#     while True:
#         entrada = input(f"Ingrese la medida del lado {nombre} (máx 40): ")
#         try:
#             valor = int(entrada)
#             if 1 <= valor <= 40:
#                 return valor
#             else:
#                 print("El valor debe ser un entero entre 1 y 40.")
#         except ValueError:
#             print("Debe ingresar un número entero.")

# # Pedir lados al usuario
# lado_a = pedir_lado("A")
# lado_b = pedir_lado("B")

# # Pedir el caracter para dibujar (opcional, por defecto "*")
# caracter = input("Ingrese el caracter para dibujar el rectángulo (por defecto *): ")
# if not caracter:
#     caracter = "*"

# # Dibujar el rectángulo
# for i in range(lado_a):
#     print(caracter * lado_b)