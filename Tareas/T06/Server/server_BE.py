import os
import random
import time
import json


class Server_BE:
    def __init__(self, server):
        self.usuarios = []
        self.server = server
        self.salas = []
        lista_carpeta = os.listdir("Songs/")
        for item in lista_carpeta:
            if os.path.isdir("Songs/"+item):
                sala = Sala(item, self)
                self.salas.append(sala)

    def desconectar(self, usuario):
        for u in self.usuarios:
            if u.name == usuario:
                self.usuarios.remove(u)
                break

    def get_info(self, name):
        for usuario in self.usuarios:
            if usuario.name == name:
                return usuario.puntos


class Usuario:
    def __init__(self, name, socket):
        self.socket = socket
        self.name = name
        self.puntos = 0
        self.sala_actual = None

    def __repr__(self):
        return self.name


class Sala:
    def __init__(self, name, server):
        self.server = server
        self.name = name
        self.usuarios = []
        self.cancion_actual = None
        self.tiempo_restante = 20
        self.tiempo_actual = 0
        self.artistas = ["Shakira", "Justin Bieber"]
        self.songs = os.listdir("Songs/"+name)
        songs = []
        for item in self.songs:
            if ".wav" in item:
                songs.append(item)
        self.songs = songs
        self.actual_song = None

    def choose_song(self):
        self.actual_song = Song(random.choice(self.songs))

    def empezar(self):
        while len(self.usuarios) > 0:
                self.choose_song()
                lista = self.songs.copy()
                actual_song = self.actual_song.name
                juego = random.choice(["titulo", "nombre"])
                if juego == "titulo":
                    lista_nueva =[]
                    for song in lista:
                        ab = song.split("-")
                        lista_nueva.append(ab)
                    lista_nueva.remove(actual_song.split("-"))
                    opcion1 = actual_song.split("-")[1].replace(".wav", "")
                    opcion2 = random.choice(lista_nueva)[1].replace(".wav", "")
                    for i in lista_nueva:
                        if opcion2 in i:
                            lista_nueva.remove(i)
                            break
                    opcion3 = random.choice(lista_nueva)[1].replace(".wav", "")
                else:
                    lista_nueva = []
                    for song in lista:
                        ab = song.split("-")
                        lista_nueva.append(ab)

                    lista_nueva.remove(actual_song.split("-"))
                    opcion1 = actual_song.split("-")[0]
                    opcion2 = random.choice(lista_nueva)[0]
                    for i in lista_nueva:
                        if opcion2 in i:
                            lista_nueva.remove(i)
                            break
                    opcion3 = random.choice(lista_nueva)[0]

                mensaje = {"accion": "comienzo_juego", "value":(self.actual_song.name, [opcion1, opcion2, opcion3])}
                print(mensaje)
                mensaje = json.dumps(mensaje)
                for users in self.server.usuarios:
                    if users.name in self.usuarios:
                        users.socket.send(mensaje.encode("utf-8"))

                while True:
                    if self.tiempo_actual <= 20:
                        self.tiempo_restante -= 1
                    elif self.tiempo_actual == 30:
                        self.tiempo_actual = 0
                        self.tiempo_restante = 20
                        break
                    time.sleep(1)
                    self.tiempo_actual += 1

    def get_info(self):
        dic = {"artistas" : self.artistas, "tiempo_restante":self.tiempo_restante, "name":self.name, "usuarios": self.usuarios}
        return dic


class Song:
    def __init__(self, name):
        self.name = name
        self.path = name
        self.data = bytearray()

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    pop = Sala("Pop")
    print(pop.songs)


