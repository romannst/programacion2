from suscripcion import Suscripcion
from playlist import Playlist
from cancion import Cancion
from dispositivo import Dispositivo

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, max_dispositivos:int, dispositivos:list = None):
        super().__init__(nombre, email, telefono)
        if not isinstance(max_dispositivos, int) or max_dispositivos <= 0:
            raise ValueError("El máximo de dispositivos debe ser un entero positivo.")
        self.__max_dispositivos = max_dispositivos
        if dispositivos != None and len(dispositivos) <= max_dispositivos:
            self.__dispositivos = dispositivos
        else:
            self.__dispositivos = list()
    
    def reproducirMusica(self):
        print("Reproduciendo música sin publicidad...")
    def descargarMusica(self):
        print("Descargando música...")
        print("Música descargada para escuchar sin conexión.")
    def elegirCancion(self, cancion:Cancion, playlist:Playlist):
        if not isinstance(cancion, Cancion):
            raise ValueError("El objeto debe ser una instancia de la clase Cancion.")
        if not isinstance(playlist, Playlist):
            raise ValueError("El objeto debe ser una instancia de la clase Playlist.")
        if cancion in playlist.obtenerCanciones():
            print(f"Reproduciendo la canción '{cancion.obtenerNombre()}' de la playlist '{playlist.obtenerNombre()}'.")
            cancion.reproducir()
        else:
            print(f"La canción '{cancion.obtenerNombre()}' no está en la playlist '{playlist.obtenerNombre()}'.")
    def habilitarDispositivo(self, dispositivo:Dispositivo):
        if not isinstance(dispositivo, Dispositivo):
            raise ValueError("El objeto debe ser una instancia de la clase Dispositivo.")
        if len(self.__dispositivos) < self.__max_dispositivos:
            self.__dispositivos.append(dispositivo)
            print(f"Dispositivo '{dispositivo.obtenerNombre()}' habilitado para la suscripción.")
        else:
            print("No se pueden habilitar más dispositivos. Se ha alcanzado el máximo permitido.")