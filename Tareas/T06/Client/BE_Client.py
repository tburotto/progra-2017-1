import main_client
import threading
import time
import json
import pickle
import random
import os
from PyQt5.QtMultimedia import QSound

class Client_Back:
    def __init__(self, front):
        self.front = front
        self.name = front.name
        self.puntos = 0
        self.cliente = main_client.Client(self)
        objetos = os.listdir("Data/")
        mensaje = {"accion": "name", "value": (self.name, objetos)}
        self.cliente.enviar_datos(mensaje)
        self.accion = {"accion": None, "value":None}

    def get_salas(self):
        msg = {"accion": "get_salas", "value": "pop"}
        self.cliente.enviar_datos(msg)

    def connect_sala(self, sala):
        msg = {"accion": "user_sala", "value": (self.name, sala)}
        self.cliente.enviar_datos(msg)

    def disconnect(self):
        mensaje = {"accion": "desconectar", "value": self.name}
        self.cliente.enviar_datos(mensaje)

    def disconnect_sala(self, sala):
        mensaje = {"accion": "desconectar_sala", "value": (self.name, sala)}
        self.cliente.enviar_datos(mensaje)

    def get_info(self):
        mensaje = {"accion": "get_info", "value": self.name}
        self.cliente.enviar_datos(mensaje)

    def chat(self, msg, sala):
        mensaje = {"accion": "chat", "value": (msg, sala, self.name)}
        self.cliente.enviar_datos(mensaje)

    def set_salas(self, salas):
        self.front.salas = salas
        print("SALAS SETTED")

    def set_chat(self, msg):
        self.front.chat.addItem(str(msg))
        print("MENSAJE RECIBIDO")

    def repr_song(self, data):
        with open("Data/song1.wav", "wb") as file:
            file.write(data)
        print("Archivo guardado")
        return

    def empezar_juego(self, value):
        self.front.song_name = "Data/"+value[0]
        lista = value[1]
        opcion1 = random.choice(lista)
        lista.remove(opcion1)
        opcion2 = random.choice(lista)
        lista.remove(opcion2)
        opcion3 = lista[0]
        time.sleep(0.4)
        self.front.opcion1.setText(opcion1)
        self.front.opcion2.setText(opcion2)
        self.front.opcion3.setText(opcion3)
        if self.front.a == 1:
            self.front.lanzar()

    def desicion(self, decision):
        mensaje = {"accion": "boton_presionado", "value":(self.front.name, self.front.sala_actual, decision)}
        self.cliente.enviar_datos(mensaje)




