from entrada import Entrada

class Visitante:
    def __init__(self, nombre:str, edad:int, estatura:float, correo_e:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero no negativo.")
        if not isinstance(estatura, (int, float)) or estatura < 0.5:
            raise ValueError("La estatura debe ser un número no negativo.")
        if not isinstance(correo_e, str) or "@" not in correo_e or ".com" not in correo_e or correo_e.strip() == "":
            raise ValueError("El correo electrónico debe ser una cadena de texto válida.")
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura
        self.__correo_e = correo_e
        self.__atracciones = list()

    def obtenerNombre(self):
        return self.__nombre
    def obtenerEdad(self):
        return self.__edad
    def obtenerEstatura(self):
        return self.__estatura
    def obtenerCorreoE(self):
        return self.__correo_e
    def atraccionesVisitadas(self)->list:
        return self.__atracciones
    def comprarEntrada(self, entrada:Entrada):
        if not isinstance(entrada, Entrada):
            raise TypeError("La entrada debe ser una instancia de la clase Entrada.")
        tipoEntrada = entrada.obtenerTipo()
        print(f"La compra de la entrada {tipoEntrada.obtenerNombre()} fue exitosa.")