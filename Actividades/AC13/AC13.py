import pickle
import json
from os import listdir
import random
import datetime as dt


def leer_usuario(data):
    usuario = Usuario()
    usuario.name = data["name"]
    usuario.contactos = data["contacts"]
    usuario.numero = data["phone_number"]
    return usuario


def leer_mensaje(data):
    mensaje = Mensaje()
    mensaje.send_by = data["send_by"]
    mensaje.send_to = data["send_to"]
    mensaje.content = data["content"]
    mensaje.last_view_date = data["last_view_date"]
    mensaje.date = data["date"]
    return mensaje


def leer_usuarios():
    lista_usuarios = []
    paths = listdir("db/usr/")
    paths.pop(0)
    for path in paths:
        with open("db/usr/"+str(path), "r") as file:
            data = json.loads(file.read(), object_hook=lambda dict_obj: leer_usuario(dict_obj))
            lista_usuarios.append(data)
    return lista_usuarios


def leer_mensajes():
    lista_mensajes = []
    paths = listdir("db/msg/")
    paths.pop(0)
    for path in paths:
        with open("db/msg/"+str(path), "r") as file:
            data = json.loads(file.read(), object_hook=lambda dict_obj: leer_mensaje(dict_obj))
            lista_mensajes.append(data)

    return lista_mensajes


def arreglar_contactos(usuarios, mensajes):
    for mensaje in mensajes:
        send_by = mensaje.send_by
        send_to = mensaje.send_to
        for usuario in usuarios:
            if usuario.numero == send_by:
                if send_to not in usuario.contactos:
                    usuario.contactos.append(send_to)
            elif usuario.numero == send_to:
                if send_by not in usuario.contactos:
                    usuario.contactos.append(send_by)


def encriptar_mensaje(mensaje, n):
    nuevo = ""
    for i in mensaje:
        num = ord(i)
        y = (num + n) % 26
        y = chr(y)
        nuevo += y
    return nuevo


def guardar_usuarios(usuarios):
    for usuario in usuarios:
        with open("secure_db/usr/"+str(usuario.numero), "w") as file:
            json_string = json.dumps(usuario.__dict__)
            file.write(json_string)


def guardar_mensajes(mensajes):
    for mensaje in mensajes:
        nombre = str(random.randint(0, 100000))
        if nombre in listdir("secure_db/msg/"):
            while nombre in listdir("secure_db/msg/"):
                nombre = str(random.randint(0, 100000))
        with open("secure_db/msg/"+nombre, "wb") as file:
            pickle.dump(mensaje, file)


def deserializar_mensaje(path):
    with open("secure_db/msg/"+str(path), "rb") as file:
        data = pickle.load(file)
    return data


class Usuario:
    def __init__(self):
        self.name = None
        self.contactos = []
        self.numero = None


class Mensaje:
    def __init__(self):
        self.send_by = None
        self.send_to = None
        self.content = None
        self.last_view_date = None
        self.date = None

    def __getstate__(self):
        encriptado = self.__dict__.copy()
        encriptado["content"] = encriptar_mensaje(encriptado["content"], self.send_by)
        return encriptado

    def __setstate__(self, state):
        state["last_view_date"] = dt.datetime.now()
        self.__dict__ = state


if __name__ == "__main__":
    usuarios = leer_usuarios()
    mensajes = leer_mensajes()
    arreglar_contactos(usuarios, mensajes)
    guardar_usuarios(usuarios)
    guardar_mensajes(mensajes)
    mensaje = deserializar_mensaje(669)
    print(mensaje.content)
