from automovil import Automovil
import random

class TestAutomovil:
    @staticmethod
    def run():
        auto = Automovil("Honda", "Civic", 2018, 220, 100)
        print("Información del automóvil:")
        print(auto.obtenerMarca(), end=", ")
        print(auto.obtenerModelo(), end=", ")
        print(auto.obtenerAnio(), end=", ")
        print(auto.obtenerVelocidadMaxima())
        cant_iteraciones = 0
        error = True
        while error:
            try:
                cant_iteraciones = int(input("Ingrese la cantidad de iteraciones a realizar: "))
                error = False
            except ValueError:
                print("Por favor, ingrese un número válido.")
        for it in range(cant_iteraciones):
            print(f"Iteracion {it + 1}")
            num_random = random.randint(0, 3)
            match num_random:
                case 0:
                    print(f"Velocidad actual: {auto.obtenerVelocidadActual()}")
                    auto.acelerar(random.randint(0, int(auto.obtenerVelocidadMaxima())))
                    print(f"Velocidad después de acelerar: {auto.obtenerVelocidadActual()}")
                case 1:
                    print(f"Velocidad actual: {auto.obtenerVelocidadActual()}")
                    auto.desacelerar(random.randint(0, int(auto.obtenerVelocidadActual())))
                    print(f"Velocidad después de desacelerar: {auto.obtenerVelocidadActual()}")
                case 2:
                    print(f"Velocidad actual: {auto.obtenerVelocidadActual()}")
                    auto.frenarPorCompleto()
                case 3:
                    minutos_para_llegar = auto.calcularMinutosParaLlegar(random.randint(1, 500))
                    print(f"Minutos para llegar a destino: {minutos_para_llegar}")
                case _:
                    pass

if(__name__ == "__main__"):
    TestAutomovil.run()