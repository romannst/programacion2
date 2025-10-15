from cancion import Cancion

class Playlist:
    def __init__(self, codigo:int, nombre:str):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__canciones = list()  # Inicializa la lista de canciones vacía

    def obtenerCodigo(self)->int:
        return self.__codigo
    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerCanciones(self)->list:
        return self.__canciones
    def agregarCancion(self, cancion:Cancion):
        if not isinstance(cancion, Cancion):
            raise ValueError("El objeto debe ser una instancia de la clase Cancion.")
        self.__canciones.append(cancion)
        print(f"Canción '{cancion.obtenerNombre()}' agregada a la playlist '{self.__nombre}'.")
    def eliminarCancion(self, cancion:Cancion):
        if not isinstance(cancion, Cancion):
            raise ValueError("El objeto debe ser una instancia de la clase Cancion.")
        if cancion in self.__canciones:
            self.__canciones.remove(cancion)
        else:
            raise ValueError("La canción no está en la playlist.")
        print(f"Canción '{cancion.obtenerNombre()}' eliminada de la playlist '{self.__nombre}'.")