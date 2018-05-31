import socket
import threading
import sys
import json
from Server import server_BE
import pickle
import time
import os
__author__ = "Tomas Burotto Clement"

PORT = 1313
IP_HOST = "127.0.0.1"

class Server:

    def __init__(self):
        self.server_name = "PrograPop"
        self.host = IP_HOST
        self.port = PORT
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_server.bind((self.host, self.port))
        self.s_server.listen(20)
        self.clientes = []
        self.BE = server_BE.Server_BE(self)
        thread = threading.Thread(target=self.aceptar, daemon=True)
        thread.setDaemon(True)
        thread.start()

    def aceptar(self):
        while len(self.clientes) < 40:
            cliente_nuevo, adress = self.s_server.accept()
            print("> Cliente_Conectado")
            self.clientes.append(cliente_nuevo)
            self.cliente_actual = cliente_nuevo
            thread_client = threading.Thread(target=self.inicio)
            thread_client.setDaemon(True)
            thread_client.start()

    def inicio(self):
        cliente = self.cliente_actual
        while True:
            time.sleep(0.2)
            try:
                data = cliente.recv(2048)
                print(data)
                data_decoded = data.decode('utf-8')
                accion = json.loads(data_decoded)
                print("data recibido")
                print(accion)

                if accion["accion"] == "name":
                    self.BE.usuarios.append(server_BE.Usuario(accion["value"][0], cliente))
                    socket_name = accion["value"]
                    lista = os.listdir("Songs/")
                    for archivo in lista:
                        if os.path.isdir("Songs/"+archivo):
                            lista2 = os.listdir("Songs/"+archivo+"/")
                            for archivo2 in lista2:
                                if ".wav" in archivo2 and archivo2 not in accion["value"][1]:
                                    data = bytearray()
                                    with open("Songs/"+archivo+"/"+archivo2, "rb") as file:
                                        for line in file:
                                            data.extend(line)
                                    cliente.send(data)
                                    time.sleep(2)
                                    mensaje = {"accion":"cancion_recibida", "value": archivo2}
                                    mensaje = json.dumps(mensaje)
                                    cliente.send(mensaje.encode("utf-8"))

                elif accion["accion"] == "desconectar":
                    self.BE.desconectar(accion["value"])
                    print("> Usuario {} desconectado".format(accion["value"]))
                    self.clientes.remove(cliente)
                    break

                elif accion["accion"] == "get_info":
                    info = self.BE.get_info(accion["value"])
                    dic = {"accion": "user_info", "value": info}
                    info_json = json.dumps(dic)
                    cliente.send(info_json.encode("utf-8"))

                elif accion["accion"] == "get_salas":
                    msg = {"accion": "sala", "value": []}
                    for sala in self.BE.salas:
                        sala = sala.get_info()
                        msg["value"].append(sala)
                    print("Mensaje a enviar {}".format(msg))
                    msg_json = json.dumps(msg)
                    cliente.send(msg_json.encode("utf-8"))

                elif accion["accion"] == "user_sala":
                    for sala in self.BE.salas:
                        if sala.name == accion["value"][1]:
                            for usuario in self.BE.usuarios:
                                if usuario.name == accion["value"][0]:
                                    sala.usuarios.append(usuario.name)
                                    if len(sala.usuarios) == 1:
                                        thread = threading.Thread(target=sala.empezar, daemon=True)
                                        thread.start()
                                usuario.sala_actual = sala.name

                elif accion["accion"] == "desconectar_sala":
                    sala1 = accion["value"][1]
                    name = accion["value"][0]
                    for sala in self.BE.salas:
                        if sala.name == sala1:
                            sala.usuarios.remove(name)

                elif accion["accion"] == "chat":
                    print("1")
                    sala1 = accion["value"][1]
                    msg = accion["value"][0]
                    name = accion["value"][2]
                    for user in self.BE.usuarios:
                        if user.sala_actual == sala1:
                            mensaje = {"accion": "chat_msg", "value": "{} : {}".format(name, msg)}
                            msg_json = json.dumps(mensaje)
                            user.socket.send(msg_json.encode("utf-8"))

                elif accion["accion"] == "boton_presionado":
                    for sala in self.BE.salas:
                        if sala.name == accion["value"][1]:
                            for usuario in sala.usuarios:
                                if usuario == accion["value"][0]:
                                    if accion["value"][2] in sala.actual_song.name:
                                        puntos = (20 - sala.tiempo_actual)*100
                                        for usr in self.BE.usuarios:
                                            if usr.name == accion["value"][0]:
                                                usr.puntos += puntos
                                                print("Usuario {} tiene ahora {}".format(usr.name, usr.puntos))

            except Exception as err:
                print(err)


if __name__ == "__main__":
    server = Server()
    while True:
        a = input("> ")