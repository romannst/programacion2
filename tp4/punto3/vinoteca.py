class Vinoteca:
    __CAPACIDAD_MAXIMA = 5000
    #constructor
    def __init__(self):
        self.__cantJugos = Vinoteca.__CAPACIDAD_MAXIMA
        self.__cantBlancos = Vinoteca.__CAPACIDAD_MAXIMA
        self.__cantTintosJovenes = Vinoteca.__CAPACIDAD_MAXIMA
        self.__cantTintosAnejados = Vinoteca.__CAPACIDAD_MAXIMA
    #comandos
    def reponerJugos(self):
        self.__cantJugos = Vinoteca.__CAPACIDAD_MAXIMA
    def reponerVinosBlancos(self):
        self.__cantBlancos = Vinoteca.__CAPACIDAD_MAXIMA
    def reponerVinosTintoJoven(self):
        self.__cantTintosJovenes = Vinoteca.__CAPACIDAD_MAXIMA
    def reponerVinosTintoAnejado(self):
        self.__cantTintosAnejados = Vinoteca.__CAPACIDAD_MAXIMA
    def venderJugos(self, unidades:int):
        if unidades >= 0:
            if unidades > self.__cantJugos:
                self.__cantJugos = 0
                print("No se pudo completar la venta, la cantidad solicitada es mayor a la disponible en la sección de jugos.")
            else:
                self.__cantJugos -= unidades
        else:
            print("Error: Ingrese un número positivo.")
    def venderVinosBlancos(self, unidades:int):
        if unidades >= 0:
            if unidades > self.__cantBlancos:
                self.__cantBlancos = 0
                print("No se pudo completar la venta, la cantidad solicitada es mayor a la disponible en la sección de vinos blancos.")
            else:
                self.__cantBlancos -= unidades
        else:
            print("Error: Ingrese un número positivo.")
    def venderVinosTintosJovenes(self, unidades:int):
        if unidades >= 0:
            if unidades > self.__cantTintosJovenes:
                self.__cantTintosJovenes = 0
                print("No se pudo completar la venta, la cantidad solicitada es mayor a la disponible en la sección de vinos tintos jóvenes.")
            else:
                self.__cantTintosJovenes -= unidades
        else:
            print("Error: Ingrese un número positivo.")
    def venderVinosTintosAnejados(self, unidades:int):
        if unidades >= 0:
            if unidades > self.__cantTintosAnejados:
                self.__cantTintosAnejados = 0
                print("No se pudo completar la venta, la cantidad solicitada es mayor a la disponible en la sección de vinos tintos añejados.")
            else:
                self.__cantTintosAnejados -= unidades
        else:
            print("Error: Ingrese un número positivo.")
    #consultas
    def obtenerCantidadJugos(self) -> int:
        return self.__cantJugos
    def obtenerCantidadVinosBlancos(self) -> int:
        return self.__cantBlancos
    def obtenerCantidadVinosTintosJovenes(self) -> int:
        return self.__cantTintosJovenes
    def obtenerCantidadVinosTintosAnejados(self) -> int:
        return self.__cantTintosAnejados