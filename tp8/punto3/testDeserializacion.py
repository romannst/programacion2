from paqueteGrupal import PaqueteGrupal
import json

class TestDeserializacion:
    @staticmethod
    def run():
        print("\nComenzando pruebas de deserializacion...\n")
        with open("./tp8/punto3/paquetes.json", "r") as file:
            dicc_paquetes = json.load(file)
            paquetes = []
            for dicc in dicc_paquetes:
                paquete = PaqueteGrupal.fromDict(dicc)
                paquetes.append(paquete)
                print(f"{paquete}\n")
        print("Deserializacion completada!")

if __name__ == "__main__":
    TestDeserializacion.run()