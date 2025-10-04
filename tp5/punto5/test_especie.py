from especie import Especie

class TestEspecie:
    @staticmethod
    def run():
        esp1 = Especie("Pandas")
        esp2 = Especie("Tortugas grandotas")
        separador = "-" * 70
        print("Valores iniciales")
        print(separador)
        print(esp1)
        print(separador)
        print(esp2)
        print(separador)
        esp1.establecerHembras(500)
        esp1.establecerMachos(500)
        esp1.establecerRitmo(0.05)
        esp2.establecerHembras(1589)
        esp2.establecerMachos(1236)
        esp2.establecerRitmo(-0.1)
        print(esp1)
        print(separador)
        print(esp2)
        print(separador)
        print(f"Años para que los pandas lleguen a 3000: {esp1.aniosParaPoblacion(3000)}")
        print(f"Años para que los pandas lleguen a 800: {esp1.aniosParaPoblacion(800)}")
        print(f"Años para que las tortugas lleguen a 3000: {esp2.aniosParaPoblacion(3000)}")
        print(f"Años para que las tortugas lleguen a 0: {esp2.aniosParaPoblacion(1)}")
        print(f"Poblacion de pandas detro de 20 años: {esp1.poblacionEstimada(20)}")
        print(f"Poblacion de tortugas detro de 20 años: {esp2.poblacionEstimada(20)}")
if __name__ == "__main__":
    TestEspecie.run()