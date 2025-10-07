from cuidador import Cuidador

class Mascota:
    def __init__(self, nombre:str, especie:str, edad:int, descripcion:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(especie, str) or especie.strip() == "":
            raise ValueError("La especie debe ser una cadena no vacía.")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero no negativo.")
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("La descripción debe ser una cadena no vacía.")
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador = None  # Inicialmente, la mascota no tiene cuidador asignado

    def asignarCuidador(self, cuidador:Cuidador):
        if not isinstance(cuidador, Cuidador):
            raise ValueError("El cuidador debe ser una instancia de la clase Cuidador.")
        self.__cuidador = cuidador
        cuidador.asignarMascota(self)
    def obtenerCuidador(self):
        if self.__cuidador is None:
            print("La mascota no tiene un cuidador asignado.")
        return self.__cuidador
    def __str__(self) -> str:
        return f"Mascota: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad}, Descripción: {self.__descripcion}, Cuidador: {self.__cuidador.obtenerNombre() if self.__cuidador else 'Sin cuidador'} Telefono: {self.__cuidador.obtenerTelefono() if self.__cuidador else '-'}"