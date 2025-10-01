from fecha import Fecha
import random

class TestFecha:
    @staticmethod
    def run():
        # Crear dos objetos Fecha
        fecha1 = Fecha(random.randint(1, 31), random.randint(1, 12), random.randint(2000, 2025))
        fecha2 = Fecha(random.randint(1, 31), random.randint(1, 12), random.randint(2000, 2025))

        # Mostrar las fechas iniciales
        print(f"Fecha 1: {fecha1}")
        print(f"Fecha 2: {fecha2}")

        # Comparar si fecha1 es anterior a fecha2
        if fecha1.esAnterior(fecha2):
            print("Fecha 1 es anterior a Fecha 2")
        else:
            print("Fecha 1 no es anterior a Fecha 2")

        # Sumar días a fecha1
        fecha1.sumaDias(3)
        print(f"Fecha 1 después de sumar 3 días: {fecha1}")

        # Obtener el día siguiente de fecha2
        dia_siguiente = fecha2.diaSiguiente()
        print(f"Día siguiente de Fecha 2: {dia_siguiente}")

        # Comparar si las dos fechas son iguales
        if fecha1.isIgualQue(fecha2):
            print("Fecha 1 es igual a Fecha 2")
        else:
            print("Fecha 1 no es igual a Fecha 2")
if __name__ == "__main__":
    TestFecha.run()