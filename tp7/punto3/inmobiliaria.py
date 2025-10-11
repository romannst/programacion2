from inmueble import Inmueble

class Inmobiliaria:
    def __init__(self, propiedades:list = None):
        if not isinstance(propiedades, list):
            raise ValueError("Propiedades debe ser una lista.")
        if propiedades != None:
            self.__propiedades = propiedades
        else:
            self.__propiedades = list()
    def insertar(self, inmueble:Inmueble):
        if not isinstance(inmueble, Inmueble) or inmueble == None:
            raise ValueError("El inmueble debe ser una instancia válida de Inmueble.")
        self.__propiedades.append(inmueble)
    def eliminar(self, inmueble:Inmueble):
        if not isinstance(inmueble, Inmueble) or inmueble == None:
            raise ValueError("El inmueble debe ser una instancia válida de Inmueble.")
        if inmueble in self.__propiedades:
            self.__propiedades.remove(inmueble)
        else:
            raise ValueError("El inmueble no se encuentra en la lista de propiedades.")
    def estaInmueble1(self, codigo:int)->bool:
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un entero positivo.")
        if not self.hayInmuebles():
            print("No hay propiedades en la inmobiliaria.")
            return False
        for inmueble in self.__propiedades:
            if inmueble.obtenerCodigo() == codigo:
                return True
        return False
    def estaInmueble2(self, inmueble:Inmueble)->bool:
        if not isinstance(inmueble, Inmueble) or inmueble == None:
            raise ValueError("El inmueble debe ser una instancia válida de Inmueble.")
        if not self.hayInmuebles():
            print("No hay propiedades en la inmobiliaria.")
            return False
        return self.esIgual(inmueble)
    def esIgual(self, inmueble:Inmueble)->bool:
        if not isinstance(inmueble, Inmueble) or inmueble == None:
            raise ValueError("El inmueble debe ser una instancia válida de Inmueble.")
        if not self.hayInmuebles():
            print("No hay propiedades en la inmobiliaria.")
            return False
        for inm in self.__propiedades:
            if inm == inmueble:
                return True
        return False
    def hayInmuebles(self)->bool:
        return len(self.__propiedades) > 0
    def contarPropiedadesMasMetros(self, metros:int)->int:
        if not isinstance(metros, int) or metros <= 0:
            raise ValueError("Los metros deben ser un entero positivo.")
        if not self.hayInmuebles():
            print("No hay propiedades en la inmobiliaria.")
            return 0
        contador = 0
        for inmueble in self.__propiedades:
            if inmueble.obtenerMetros2() > metros:
                contador += 1
        return contador
    def mayorPrecioVenta(self, m2:float)->Inmueble:
        if not self.hayInmuebles():
            raise ValueError("No hay propiedades en la inmobiliaria.")
        p_mayor = self.__propiedades[0]
        for inmueble in self.__propiedades:
            if inmueble.precioVenta(m2) > p_mayor.precioVenta(m2):
                p_mayor = inmueble
        return p_mayor
    def costoMenorQue(self, costo:int, base:int)->"Inmobiliaria":
        if not isinstance(costo, int) or costo <= 0:
            raise ValueError("El costo debe ser un entero positivo.")
        if not self.hayInmuebles():
            print("No hay propiedades en la inmobiliaria.")
            return Inmobiliaria()
        nueva_inmobiliaria = Inmobiliaria()
        for inmueble in self.__propiedades:
            if inmueble.costoAlquiler(base) < costo:
                nueva_inmobiliaria.insertar(inmueble)
        return nueva_inmobiliaria