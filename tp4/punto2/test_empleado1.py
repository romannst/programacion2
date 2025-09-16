from empleado import Empleado

class TestEmpleado:
    @staticmethod
    def run():
        #quiero que el usuario ingrese los datos de un empleado
        error = True
        legajo1, legajo2 = 0, 0
        horas1, horas2 = 0, 0
        valor1, valor2 = 0.0, 0.0
        while error:
            try:
                legajo1 = int(input("Ingrese su legajo: "))
                horas1 = int(input("Ingrese las horas trabajadas: "))
                valor1 = float(input("Ingrese el valor de cada hora: "))
                legajo2 = int(input("Ingrese su legajo: "))
                horas2 = int(input("Ingrese las horas trabajadas: "))
                valor2 = float(input("Ingrese el valor de cada hora: "))
                error = False
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese los datos nuevamente.")
        empleado1 = Empleado(legajo1, horas1, valor1)
        empleado2 = Empleado(legajo2, horas2, valor2)
        print(f"Empleado 1 - Legajo: {empleado1.obtenerLegajo()}, Sueldo: {empleado1.obtenerSueldo():.2f}")
        print(f"Empleado 2 - Legajo: {empleado2.obtenerLegajo()}, Sueldo: {empleado2.obtenerSueldo():.2f}")

if __name__ == "__main__":
    TestEmpleado.run()