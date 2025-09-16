from empleado import Empleado

class TestEmpleado:
    @staticmethod
    def run():
        #quiero que el usuario ingrese los datos de un empleado
        error = True
        legajo, horas, valor = 0, 0, 0.0
        while error:
            try:
                legajo = int(input("Ingrese su legajo: "))
                horas = int(input("Ingrese las horas trabajadas: "))
                valor = float(input("Ingrese el valor de cada hora: "))
                error = False
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese los datos nuevamente.")
        empleado = Empleado(legajo)
        empleado.establecerHorasTrabajadas(horas)
        empleado.establecerValorHora(valor)
        print(f"Empleado - Legajo: {empleado.obtenerLegajo()}, Sueldo: {empleado.obtenerSueldo():.2f}")

if __name__ == "__main__":
    TestEmpleado.run()