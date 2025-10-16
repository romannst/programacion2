from profesor import Profesor
from estudiante import Estudiante
from curso import Curso
from clase import Clase

class TestEscuela:
    @staticmethod
    def run():
        # Creación de objetos
        print("Creando objetos...\n")
        
        profesor1 = Profesor(1, "Carlos Pérez", "Matemáticas")
        profesor2 = Profesor(2, "Laura González", "Historia")
        print(profesor1)
        print("-"*40)
        print(profesor2)
        print("-"*40)
        print("-"*40)
        estudiante1 = Estudiante(101, "Juan López", "2003-05-12")
        estudiante2 = Estudiante(102, "Ana García", "2004-07-19")
        print(estudiante1)
        print("-"*40)
        print(estudiante2)
        print("-"*40)
        print("-"*40)
        curso1 = Curso(101, "Matemáticas Básicas", profesor1)
        curso2 = Curso(202, "Historia Universal", profesor2)
        print(curso1)
        print("-"*40)
        print(curso2)
        print("-"*40)
        print("-"*40)
        # Modificaciones de atributos
        print("Modificando atributos...\n")
        profesor1.nuevaEspecialidad("Física")
        print(profesor1)
        print("-"*40)
        # Asignaciones iniciales
        print("Inscribiendo estudiantes en cursos...\n")
        estudiante1.inscribirse(curso1)
        estudiante2.inscribirse(curso1)
        estudiante2.inscribirse(curso2)
        print(estudiante1.obtenerNombre(), "está inscrito en:")
        print(estudiante1.cursosInscripto())
        print("-"*40)
        print(estudiante2.obtenerNombre(), "está inscrito en:")
        print(estudiante2.cursosInscripto())
        print("-"*40)
        print("-"*40)        
        # Cambiando objetos entre atributos (asignación)
        print("\nCambiando asignaciones entre objetos...\n")
        profesor2 = profesor1  # Ahora profesor2 es el mismo que profesor1
        print(f"Profesor 2 ahora es: {profesor2.obtenerNombre()}")
        estudiante2 = estudiante1  # Ahora estudiante2 es el mismo que estudiante1
        print(f"Estudiante 2 ahora es: {estudiante2.obtenerNombre()}")
        curso2 = curso1  # Ahora curso2 es el mismo que curso1
        print(f"Curso 2 ahora es: {curso2.obtenerNombre()}")
        print("-"*40)
        print("-"*40)
        # Creación de una clase
        print("Creando una clase...\n")
        clase1 = Clase("2024-10-01", "10:00", curso1)
        print("Clase 1:")
        print(clase1)
        print("-"*40)
        clase2 = Clase("2024-10-02", "14:00", curso2)
        print("Clase 2:")
        print(clase2)
if __name__ == "__main__":
    TestEscuela.run()