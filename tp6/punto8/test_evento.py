from evento import Evento
from fecha import Fecha
from organizador import Organizador
from participante import Participante

class TestEvento:
    @staticmethod
    def run():
        evento1 = Evento("Concierto de Rock", Fecha(2023, 10, 15), "Auditorio Nacional")
        print(evento1)
        evento2 = Evento("Conferencia de Tecnología", Fecha(2023, 11, 20), "Centro de Convenciones")
        print(evento2)
        #testear funciones de la clase Evento\
        evento1.asignarOrganizador(Organizador("Juan", "juan@example.com", "Música"))
        evento1.agregarParticipante(Participante("Ana", "ana@example.com", "123456789"))
        print(evento1)


if __name__ == "__main__":
    TestEvento.run()