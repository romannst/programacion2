from atleta import Atleta
import random

class TestAtleta:
    @staticmethod
    def run():
        atleta1 = Atleta("Juan")
        atleta2 = Atleta("Maria")
        while atleta1.obtenerDestreza() < random.randint(1, 10) and atleta2.obtenerDestreza() < random.randint(1, 10):
            if random.choice([True, False]):
                atleta1.entrenar()
            else:
                atleta1.descansar()
            if random.choice([True, False]):
                atleta2.entrenar()
            else:
                atleta2.descansar()
        if atleta1.mismaDestrezaQue(atleta2):
            print(f"Ambos atletas tienen la misma destreza.")
        else:
            if atleta1.mayorDestrezaQue(atleta2):
                print(f"{atleta1.obtenerNombre()} tiene mayor destreza que {atleta2.obtenerNombre()}.")
            elif atleta2.mayorDestrezaQue(atleta1):
                print(f"{atleta2.obtenerNombre()} tiene mayor destreza que {atleta1.obtenerNombre()}.")
        print(atleta1)
        print(atleta2)
if __name__ == "__main__":
    TestAtleta.run()