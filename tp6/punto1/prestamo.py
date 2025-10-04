from fecha import Fecha
from libro import Libro
from socio import Socio

class Prestamo:
    def __init__(self, libro:Libro, fechaPrestamo:Fecha, cantDias:int, socio:Socio):
        if not isinstance(libro, Libro):
            raise TypeError("El libro debe ser una instancia de la clase Libro")
        if not isinstance(fechaPrestamo, Fecha):
            raise TypeError("La fecha de préstamo debe ser una instancia de la clase Fecha")
        if not isinstance(cantDias, int) or cantDias <= 0:
            raise ValueError("La cantidad de días debe ser un entero positivo")
        if not isinstance(socio, Socio):
            raise TypeError("El socio debe ser una instancia de la clase Socio")
        self.__libro = libro
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = cantDias
        self.__socio = socio
        self.__fechaDevolucion = None
    def establecerFechaDevolucion(self, fechaDev:Fecha):
        self.__fechaDevolucion = fechaDev
        if self.__fechaDevolucion is not None:
            penal = self.penalizacion()
            if penal is not None:
                self.__socio.establecerFechaPenalizacion(penal)
    def obtenerLibro(self)->Libro:
        return self.__libro
    def obtenerFechaPrestamo(self)->Fecha:
        return self.__fechaPrestamo
    def obtenerFechaDevolucion(self)->Fecha:
        if self.__fechaDevolucion is None:
            raise ValueError("El libro no ha sido devuelto aún")
        return self.__fechaDevolucion
    def estaAtrasado(self, fecha:Fecha)->bool:
        if not isinstance(fecha, Fecha):
            raise TypeError("La fecha debe ser una instancia de la clase Fecha")

        # Calcular el plazo límite de devolución
        plazo_devolucion = self.__fechaPrestamo.sumaDias(self.__dias)

        # Verificar si la fecha actual ya está en el plazo de devolución
        return plazo_devolucion.esAnterior(fecha)
    def penalizacion(self):
        if self.__fechaDevolucion is None:
            raise ValueError("El libro no ha sido devuelto aún")
        
        # Fecha límite de devolución
        plazo_devolucion = self.__fechaPrestamo.sumaDias(self.__dias)

        # Verificar si está atrasado
        if not plazo_devolucion.esAnterior(self.__fechaDevolucion):
            return None  # No hay penalización

        # Calcular los días de atraso
        diasAtraso = self.dias_absolutos(self.__fechaDevolucion) - self.dias_absolutos(plazo_devolucion)

        # Determinar la penalización
        if diasAtraso < 7:
            dias_penalizacion = 3
        elif diasAtraso < 21:
            dias_penalizacion = 5
        else:
            dias_penalizacion = 10

        # Si el libro es de categoría 'A', duplicar penalización
        if self.__libro.obtenerCategoria().upper() == 'A':
            dias_penalizacion *= 2

        # Calcular la fecha de penalización sumando los días de penalización a la fecha de devolución
        fecha_penalizacion = self.__fechaDevolucion.sumaDias(dias_penalizacion)
        return fecha_penalizacion
    
    def __str__(self)->str:
        return (f"Préstamo del libro: {self.__libro}\n"
                f"Prestado a: {self.__socio}\n"
                f"Fecha de préstamo: {self.__fechaPrestamo}\n"
                f"Días de préstamo: {self.__dias}\n"
                f"Fecha de devolución: {self.__fechaDevolucion if self.__fechaDevolucion else 'No devuelto aún'}")

    def dias_absolutos(self, fecha:Fecha)->int:
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dias = fecha.obtenerAnio() * 365
        # Sumar años bisiestos
        bisiestos = (fecha.obtenerAnio() // 4) - (fecha.obtenerAnio() // 100) + (fecha.obtenerAnio() // 400)
        dias += bisiestos
        # Sumar los meses completos del año actual
        for m in range(1, fecha.obtenerMes()):
            dias += dias_por_mes[m - 1]
            # Si es febrero y el año es bisiesto, sumar un día más
            if m == 2 and ((fecha.obtenerAnio() % 4 == 0 and fecha.obtenerAnio() % 100 != 0) or (fecha.obtenerAnio() % 400 == 0)):
                dias += 1
        # Sumar los días del mes actual
        dias += fecha.obtenerDia()
        return dias