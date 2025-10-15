from evento import Evento
from fecha import Fecha
from organizador import Organizador
from participante import Participante

class TestEvento:
    @staticmethod
    def run():
        evento1 = Evento("Concierto de Rock", Fecha(15, 10, 2023), "Auditorio Nacional")
        evento2 = Evento("Conferencia de Tecnología", Fecha(20, 11, 2023), "Centro de Convenciones")
        print(evento1)
        print(evento2)
        print("-"*40)
        #agregar 5 participantes
        evento1.agregarParticipante(Participante("Ana", "ana@example.com", "123456789"))
        evento1.agregarParticipante(Participante("Luis", "luis@example.com", "987654321"))
        evento1.agregarParticipante(Participante("Maria", "maria@example.com", "456789123"))
        evento1.agregarParticipante(Participante("Pedro", "pedro@example.com", "321654987"))
        evento1.agregarParticipante(Participante("Sofia", "sofia@example.com", "159753486"))
        #agregar organizador
        evento1.asignarOrganizador(Organizador("Carlos", "carlos@example.com", "Música"))
        print(evento1)
        #lo mismo para evento2
        evento2.agregarParticipante(Participante("Jorge", "jorge@example.com", "123123123"))
        evento2.agregarParticipante(Participante("Ana", "ana@example.com", "123456789"))
        evento2.agregarParticipante(Participante("Luis", "luis@example.com", "987654321"))
        evento2.agregarParticipante(Participante("Maria", "maria@example.com", "456789123"))
        evento2.agregarParticipante(Participante("Pedro", "pedro@example.com", "321654987"))
        evento2.agregarParticipante(Participante("Sofia", "sofia@example.com", "159753486"))
        evento2.asignarOrganizador(Organizador("Laura", "laura@example.com", "Tecnología"))
        print(evento2)

if __name__ == "__main__":
    TestEvento.run()