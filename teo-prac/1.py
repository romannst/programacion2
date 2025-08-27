#for
personas = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
for p in personas:
    print(f"Hola {p}")
for p in range(len(personas)):
    print(f"Hola {personas[p]}")

#funciones
def funcion():
    print("Hola")
def funcion_saludo(nombre):
    print(f"Hola {nombre}")
funcion()
funcion_saludo("Pepito")
funcion_saludo("Pepito" + " Gomez")
funcion_saludo(input("Ingrese su nombre: "))
def sumar(a, b):
    total = a + b
    return total
suma = sumar(int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: ")))
print(f"La suma es: {suma}")
def sumar(a:int, b:int) -> int:
    total = a + b
    return total
def funcion_saludo(nombre:str):
    print(f"Hola {nombre}")

#listas
lista_vacia = []
lista_vacia = list()
lista_int = [1, 2, 3]
lista_mixed = [1, "dos", 3.45]
print(2 in lista_int)
print(2 in lista_mixed)
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Indice de 4: {lista.index(4)}")
print(lista[:]) # == print(lista)
print(lista[0:2])
print(lista[2:5])
print(lista[5:8]) # == print(lista[5:])
lista_aux = lista # referencia a la misma lista
lista_aux = lista.copy() # referencia a una copia de la lista
lista.append(9) # agrega 9 al final de la lista
lista.insert(0, 0) # inserta 0 al inicio de la lista
lista.index(3) # devuelve el índice del primer elemento con valor 3
lista.pop(len(lista)-1) # elimina el último elemento de la lista
lista.remove(2) # elimina el primer elemento con valor 2
lista.sort() # ordena la lista de menor a mayor
lista.sort(reverse=True) # ordena la lista de mayor a menor

#ejercicio
# Generar una lista con los elementos pares múltiplos de 3, menores a un número ingresado por el usuario.
# Dividir el problema en subproblemas.
#sol1
numero = int(input("Ingrese un número: "))
lista_elems = list() # lista vacía
def elementos_pares_multiplos_de_tres(numero):
    aux = 3
    while (aux < numero):
        if(aux % 2 == 0):
            lista_elems.append(aux)
        aux += 3
    return lista_elems
lista_resultado = elementos_pares_multiplos_de_tres(numero)
print(f"Lista: {lista_resultado}")
#sol2
def leer_entero(mensaje:str)->int:
    repetir = True
    while repetir:
        try:
            ingreso = input(mensaje)
            numero = int(ingreso)
            repetir=False            
        except ValueError:
            print('Error, debe ingresar un número entero.')
            print('Inténtelo nuevamente:')
    return numero
lista_pares = []
limite = -1
while limite < 0:
    limite = leer_entero("Ingrese un número entero positivo: ")
for i in range(0, limite):
    if i%3==0 and i%2==0:
        lista_pares.append(i)
print(lista_pares)
#ejercicio
#Tenemos cargada una lista con las notas del primer parcial. El profesor decide cambiar el puntaje de un punto, y eso implica darles 5 puntos más a cada nota porque todos tenían bien ese punto.
notas = [80, 60, 75, 100, 55, 35]
notas_ajustadas = notas.copy()
for i in range(len(notas_ajustadas)):
    if notas_ajustadas[i] > 95:
        notas_ajustadas[i] = 100
    else:
        notas_ajustadas[i] += 5
print("notas ajustadas", notas_ajustadas)
print("notas originales", notas)

#diccionarios
mochila = dict() # == mochila = {}
mochila["libros"] = 5
mochila["lapices"] = 10
mochila["cuadernos"] = 3
print(mochila)
print(mochila["libros"])

#archivos
#ej1
archivo = open("archivo.txt", "r")
for linea in archivo:
    print(linea)
archivo.close()
#ej2
ruta = r"C:\Users\Roman\programacion2\teo-prac\archivo.txt"
archivo = open(ruta, "r")
contador = 0
for linea in archivo:
    contador += 1
print("Lineas:", contador)
archivo.close()
#ej3
ruta = r"C:\Users\Roman\programacion2\teo-prac\archivo.txt"
archivo = open(ruta, "r")
lista_lineas = archivo.readlines() 
print("Lineas:", len(lista_lineas))
archivo.close()
#manejo seguro de archivos
FILE_PATH = r"c:\Programacion2\datos.txt"
with open(FILE_PATH, "r") as file:
	for line in file:
    		print(line)