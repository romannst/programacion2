import json
from libro import Libro

class TestLibro:
    @staticmethod
    def run():
        #como cargo los datos del JSON libros.json en objetos de clase Libro
        print("Cargando datos de libros desde libros.json...\n")
        with open("./tp8/punto1/libros.json", "r", encoding="utf-8") as file:
            #carga el contenido del archivo JSON en una lista de diccionarios
            data = json.load(file) # json.load devuelve una lista de diccionarios
            libros = []
            #convierte cada diccionario en un objeto Libro usando el método fromDict
            for data_libro in data:
                libro = Libro.fromDict(data_libro) #fromDict hace la deserialización del diccionario al objeto libro
                libros.append(libro) #agrega el objeto libro a la lista de libros
            print("Datos cargados exitosamente. Libros disponibles:\n")
            for libro in libros:
                print(f"Libro {libro.obtener_titulo()} de {libro.obtener_autor()}:")
                print(libro.toDict(), end="\n\n") #toDict hace la serialización del objeto libro al diccionario
        print("Búsqueda de libros por año de publicación:")
        anio_a_buscar = int(input("Ingrese el año de publicación a buscar: ")) #solicita al usuario el año a buscar
        for libro in libros:
            if libro.obtener_anio_publicacion() == anio_a_buscar:
                print(f"Libro encontrado: {libro.obtener_titulo()} de {libro.obtener_autor()}")
                
if __name__ == "__main__":
    TestLibro.run()