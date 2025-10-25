import json
from contacto import Contacto

class TestContacto:
    @staticmethod
    def run():
        #crear objetos de la clase Contacto, parametros: nombre:str, apellido:str, telefono:str, correo_e:str, direccion:str
        print("Creando y guardando contactos en contactos.json...\n")
        contacto1 = Contacto("Juan", "Perez", "123456789", "juan.perez@example.com", "Calle Falsa 123")
        contacto2 = Contacto("Maria", "Gomez", "987654321", "maria.gomez@example.com", "Avenida Siempre Viva 742")
        contacto3 = Contacto("Luis", "Martinez", "456789123", "luis.martinez@example.com", "Boulevard de los Sueños Rotos 456")
        contacto4 = Contacto("Ana", "Lopez", "321654987", "ana.lopez@example.com", "Calle de la Amargura 321")
        contacto5 = Contacto("Carlos", "Sanchez", "654321789", "carlos.sanchez@example.com", "Avenida de la Paz 123")
        contacto6 = Contacto("Laura", "Ramirez", "789123456", "laura.ramirez@example.com", "Calle de la Ilusión 789")
        contacto7 = Contacto("Pedro", "Martinez", "159753486", "pedro.martinez@example.com", "Calle de la Amargura 123")
        contacto8 = Contacto("Sofia", "Martinez", "753159486", "sofia.martinez@example.com", "Calle de la Ilusión 123")
        lista_contactos = [contacto1, contacto2, contacto3, contacto4, contacto5, contacto6, contacto7, contacto8]

        #guardar la lista de contactos en un archivo JSON "contactos.json"
        print("Guardando contactos en contactos.json...\n")
        with open("./tp8/punto2/contactos.json", "w") as file: #abro un archivo "contactos.json" en modo escritura
            #guardo cada contacto como un diccionario en una lista de diccionarios
            diccionarios_contactos = [contacto.toDict() for contacto in lista_contactos]
            #guardo la lista de diccionarios en el archivo JSON
            json.dump(diccionarios_contactos, file, ensure_ascii=False, indent=4)
        
        nueva_lista_contactos = []
        #leer la lista de contactos desde el archivo JSON "contactos.json"
        print("Cargando contactos desde contactos.json...\n")
        with open("./tp8/punto2/contactos.json", "r") as file: #abro el archivo "contactos.json" en modo lectura
            #cargo la lista de diccionarios desde el archivo JSON
            diccionarios_contactos = json.load(file)
            #creo un objeto Contacto por cada diccionario y lo agrego a la nueva lista de contactos
            for dic in diccionarios_contactos:
                contacto = Contacto.fromDict(dic) #fromDict para guardar el diccionario en un objeto Contacto
                nueva_lista_contactos.append(contacto) #agrego el objeto Contacto a la nueva lista de contactos

        print("Busqueda de contactos por letra inicial del apellido:")
        letra_apellido = input("Ingrese una letra para filtrar contactos por apellido: ").strip().lower()
        cant_encontrados = 0
        contactos_encontrados = ""
        for contacto in nueva_lista_contactos:
            if contacto.obtener_apellido()[0].lower() == letra_apellido:
                cant_encontrados += 1
                contactos_encontrados += "Nombre: " + contacto.obtener_nombre() + " " + contacto.obtener_apellido() + "\n" + "Email: " + contacto.obtener_correo_e() + "\n" + "-"*40 + "\n"
        print(f"\nSe encontraron {cant_encontrados} contactos con apellido que comienza con la letra '{letra_apellido}':") if cant_encontrados > 1 else print(f"\nSe encontró {cant_encontrados} contacto con apellido que comienza con la letra '{letra_apellido}':")
        print(contactos_encontrados) if cant_encontrados > 0 else print("No se encontraron contactos.")
if __name__ == "__main__":
    TestContacto.run()