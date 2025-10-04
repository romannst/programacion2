from prestamo import Prestamo
from libro import Libro
from socio import Socio
from fecha import Fecha
import random

class TestPrestamo:
    @staticmethod
    def run1():
        #testear los servicios de la clase Prestamo
        libro = Libro("El Quijote", "Miguel de Cervantes", "Penguin Classics", "A")
        socio = Socio("Juan Perez", Fecha(15, 5, 1990))
        fecha_prestamo = Fecha(1, 3, 2024)
        prestamo = Prestamo(libro, fecha_prestamo, 14, socio)
        print(prestamo)
        print("\n")
        if prestamo.estaAtrasado(Fecha(20, 3, 2024)):
            print("Si el libro se devuelve el 20 de marzo de 2024, el préstamo estará atrasado.")
        # Establecer fecha de devolución
        prestamo.establecerFechaDevolucion(Fecha(20, 3, 2024))  # Devuelto con atraso
        print("\n")
        print(prestamo)
    @staticmethod
    def run2():
        #testear los servicios de la clase Prestamo con datos que ingresa el usuario
        libro = Libro(input("Ingrese el título del libro: "), input("Ingrese el autor del libro: "), input("Ingrese la editorial del libro: "), input("Ingrese la ubicación del libro: "))
        socio = Socio(input("Ingrese el nombre del socio: "), Fecha(int(input("Ingrese el día de nacimiento: ")), int(input("Ingrese el mes de nacimiento: ")), int(input("Ingrese el año de nacimiento: "))))
        fecha_prestamo = Fecha(int(input("Ingrese el día del préstamo: ")), int(input("Ingrese el mes del préstamo: ")), int(input("Ingrese el año del préstamo: ")))
        prestamo = Prestamo(libro, fecha_prestamo, int(input("Ingrese la cantidad de días de préstamo: ")), socio)
        print(prestamo)
        print("\n")
        # Establecer fecha de devolución
        fecha_devolucion = Fecha(int(input("Ingrese el día de devolución: ")), int(input("Ingrese el mes de devolución: ")), int(input("Ingrese el año de devolución: ")))
        prestamo.establecerFechaDevolucion(fecha_devolucion)  # Devuelto con atraso
        if prestamo.estaAtrasado(fecha_devolucion):
            print(f"Si el libro se devuelve en la fecha {fecha_devolucion}, el préstamo estará atrasado.")
        print("\n")
        print(prestamo)

if __name__ == "__main__":
    num_random = random.randint(1, 2)
    if num_random == 1:
        TestPrestamo.run1()
    else:
        TestPrestamo.run2()