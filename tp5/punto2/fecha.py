class Fecha:
    def __init__(self, dia:int, mes:int, anio:int):
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anio, int) :
            raise TypeError("Día, mes y año deben ser enteros.")
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 1:
            raise ValueError("Día, mes o año fuera de rango.")
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def establecerDia(self, dia:int):
        self.dia = dia
    def establecerMes(self, mes:int):
        self.mes = mes
    def establecerAnio(self, anio:int):
        self.anio = anio
    def obtenerDia(self)->int:
        return self.dia
    def obtenerMes(self)->int:
        return self.mes
    def obtenerAnio(self)->int:
        return self.anio
    def esAnterior(self, otraFecha:"Fecha")->bool:
        if self.anio < otraFecha.obtenerAnio():
            return True
        if self.anio == otraFecha.obtenerAnio():
            if self.mes < otraFecha.obtenerMes():
                return True
            if self.mes == otraFecha.obtenerMes():
                return self.dia < otraFecha.obtenerDia()
        return False
    def sumaDias(self, cantDias:int)->"Fecha":
        if cantDias < 0:
            raise ValueError("La cantidad de días a sumar no puede ser negativa.")
        match self.mes:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                #enero, marzo, mayo, julio, agosto, octubre, diciembre 31 dias
                if self.dia + cantDias > 31:
                    self.dia = (self.dia + cantDias) - 31
                    if self.mes == 12:
                        self.mes = 1
                        self.anio += 1
                    else:
                        self.mes += 1
                else:
                    self.dia += cantDias
            case 4 | 6 | 9 | 11:
                #abril, junio, septiembre, noviembre 30 dias
                if self.dia + cantDias > 30:
                    self.dia = (self.dia + cantDias) - 30
                    self.mes += 1
                else:
                    self.dia += cantDias
            case 2:
                #febrero 28 dias
                if self.dia + cantDias > 28:
                    self.dia = (self.dia + cantDias) - 28
                    self.mes += 1
                else:
                    self.dia += cantDias
            case _:
                raise ValueError("Mes inválido")
        return self
    def diaSiguiente(self)->"Fecha":
        return self.sumaDias(1)
    def isIgualQue(self, otraFecha:"Fecha")->bool:
        return self.dia == otraFecha.obtenerDia() and self.mes == otraFecha.obtenerMes() and self.anio == otraFecha.obtenerAnio()
    def __str__(self) -> str:
        fecha = f"{self.dia:02}/{self.mes:02}/{self.anio}"
        return fecha