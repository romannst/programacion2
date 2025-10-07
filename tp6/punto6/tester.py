from disciplina import Disciplina
from participante import Participante

class Tester:
    @staticmethod
    def run():
        print("---------- Menu de Disciplinas ----------")
        print("1. Agregar disciplina")
        print("0. Salir")
        num = int(input("Ingrese la opción deseada: "))
        disciplinas = list()
        #ingreso de disciplinas
        while isinstance(num, int) and num == 1:
            nombre = input("Ingrese el nombre de la disciplina: ")
            descripcion = input("Ingrese la descripción de la disciplina: ")
            disciplina = Disciplina(nombre, descripcion)
            disciplinas.append(disciplina)
            print(f"Disciplina '{nombre}' creada.")
            num = int(input("Ingrese 1 para agregar otra disciplina o 0 para salir: "))
        print("---------- Menu de Participantes ----------")
        print("1. Agregar participante")
        print("0. Salir")
        num = int(input("Ingrese la opción deseada: "))
        participantes = list()
        #ingreso de participantes
        while isinstance(num, int) and num == 1:
            nombre = input("Ingrese el nombre del participante: ")
            edad = int(input("Ingrese la edad del participante: "))
            nacionalidad = input("Ingrese la nacionalidad del participante: ")
            participante = Participante(nombre, edad, nacionalidad)
            participantes.append(participante)
            print(f"Participante '{nombre}' agregado.")
            print("Disciplinas disponibles:")
            corte = False
            cant_disciplinas = len(disciplinas)
            i = 0
            while cant_disciplinas > 0 and i < cant_disciplinas and not corte:
                print(f"{i+1}. {disciplinas[i].obtener_nombre()}")
                opcion = input("Si desea inscribirse en esta disciplina ingrese 's', de lo contrario ingrese 'n': ").lower()
                if isinstance(opcion, str):
                    if opcion == 's':
                        participante.agregar_disciplina(disciplinas[i])
                        print(f"{participante.obtener_nombre()} inscrito en {disciplinas[i].obtener_nombre()}.")
                        i += 1
                    elif opcion == 'n':
                        opcion = input("Si desea seguir viendo otras disciplinas ingrese 's', de lo contrario ingrese 'n': ").lower()
                        if opcion == 's':
                            i += 1
                        else:
                            corte = True
                    else:
                        print("Opción no válida. Saliendo del menú de inscripción.")
                        corte = True
            num = int(input("Ingrese 1 para agregar otro participante o 0 para salir: "))
        if len(disciplinas) == 0 or len(participantes) == 0:
            if len(disciplinas) == 0:
                print("No se han creado disciplinas.")
            if len(participantes) == 0:
                print("No se han agregado participantes.")
        else:
            print("---------- Resumen de Disciplinas y Participantes ----------")
            print("Participantes inscriptos en cada disciplina:")
            for disciplina in disciplinas:
                disciplina.mostrar_participantes()
            print("Disciplinas en las que está inscripto cada participante:")
            for participante in participantes:
                participante.mostrar_disciplinas()

if __name__ == "__main__":
    Tester.run()