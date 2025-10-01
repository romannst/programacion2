class Fecha:
    def __init__(self, dia:int, mes:int, anio:int):
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anio, int) :
            raise TypeError("Día, mes y año deben ser enteros.")
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1:
            raise ValueError("Día, mes o año fuera de rango.")
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    def establecerDia(self, dia:int):
        self.__dia = dia
    def establecerMes(self, mes:int):
        self.__mes = mes
    def establecerAnio(self, anio:int):
        self.__anio = anio
    def obtenerDia(self)->int:
        return self.__dia
    def obtenerMes(self)->int:
        return self.__mes
    def obtenerAnio(self)->int:
        return self.__anio
    def esAnterior(self, otraFecha:"Fecha")->bool:
        if not isinstance(otraFecha, Fecha):
            raise TypeError("El parámetro debe ser una instancia de Fecha.")
        if self.__anio < otraFecha.obtenerAnio():
            return True
        if self.__anio == otraFecha.obtenerAnio():
            if self.__mes < otraFecha.obtenerMes():
                return True
            if self.__mes == otraFecha.obtenerMes():
                return self.__dia < otraFecha.obtenerDia()
        return False
    def sumaDias(self, cantDias:int)->"Fecha":
        if not isinstance(cantDias, int):
            raise TypeError("La cantidad de días a sumar debe ser un entero.")
        elif cantDias < 0:
            raise ValueError("La cantidad de días a sumar no puede ser negativa.")
        match self.__mes:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                #enero, marzo, mayo, julio, agosto, octubre, diciembre 31 dias
                if self.__dia + cantDias > 31:
                    self.__dia = (self.__dia + cantDias) - 31
                    if self.__mes == 12:
                        self.__mes = 1
                        self.__anio += 1
                    else:
                        self.__mes += 1
                else:
                    self.__dia += cantDias
            case 4 | 6 | 9 | 11:
                #abril, junio, septiembre, noviembre 30 dias
                if self.__dia + cantDias > 30:
                    self.__dia = (self.__dia + cantDias) - 30
                    self.__mes += 1
                else:
                    self.__dia += cantDias
            case 2:
                #febrero 28 dias
                if self.__dia + cantDias > 28:
                    self.__dia = (self.__dia + cantDias) - 28
                    self.__mes += 1
                else:
                    self.__dia += cantDias
            case _:
                raise ValueError("Mes inválido")
        return self
    def diaSiguiente(self)->"Fecha":
        return self.sumaDias(1)
    def isIgualQue(self, otraFecha:"Fecha")->bool:
        if not isinstance(otraFecha, Fecha):
            raise TypeError("El parámetro debe ser una instancia de Fecha.")
        return self.__dia == otraFecha.obtenerDia() and self.__mes == otraFecha.obtenerMes() and self.__anio == otraFecha.obtenerAnio()
    def __str__(self) -> str:
        fecha = f"{self.__dia:02}/{self.__mes:02}/{self.__anio}"
        return fecha