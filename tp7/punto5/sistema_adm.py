class Personal:
    def __init__(self, nombre, apellido, dni):
        # Atributos protegidos (accesibles desde subclases)
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido
    def getDNI(self):
        return self._dni
    def setNombre(self, nombre):
        self._nombre = nombre
    def setApellido(self, apellido):
        self._apellido = apellido
    def setDNI(self, dni):
        self._dni = dni

class Administrativo(Personal):
    def __init__(self, nombre, apellido, dni, legajo, posicion):
        super().__init__(nombre, apellido, dni)
        # Atributos privados de la subclase (no accesibles fuera de la clase)
        self.__legajo = legajo
        self.__posicion = posicion

    def getLegajo(self):
        return self.__legajo
    def getPosicion(self):
        return self.__posicion
    def setLegajo(self, legajo):
        self.__legajo = legajo
    def setPosicion(self, posicion):
        self.__posicion = posicion

class Programador(Personal):
    def __init__(self, nombre, apellido, dni, legajo, proyecto):
        super().__init__(nombre, apellido, dni)
        # Atributos privados de la subclase
        self.__legajo = legajo
        self.__proyecto = proyecto

    def getLegajo(self):
        return self.__legajo
    def getProyecto(self):
        return self.__proyecto
    def setLegajo(self, legajo):
        self.__legajo = legajo
    def setProyecto(self, proyecto):
        self.__proyecto = proyecto

class PersonalMantenimiento(Personal):
    def __init__(self, nombre, apellido, dni, legajo, area):
        super().__init__(nombre, apellido, dni)
        # Atributos privados de la subclase
        self.__legajo = legajo
        self.__area = area

    def getLegajo(self):
        return self.__legajo
    def getArea(self):
        return self.__area
    def setLegajo(self, legajo):
        self.__legajo = legajo
    def setArea(self, area):
        self.__area = area