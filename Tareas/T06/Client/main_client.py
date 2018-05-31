import socket
import threading
import json
import sys
import pickle

__author__ = 'Tomas Burotto Clement'

PORT = 13134
IP_SERVER = "192.168.1.102"


class Client:
    def __init__(self, Back):
        self.BE = Back
        self.host = IP_SERVER
        self.port = PORT
        self.accion = {}
        self.s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bytes = bytearray()
        try:
            self.s_client.connect((self.host, self.port))
            recibidor = threading.Thread(target=self.recibir, args=())
            recibidor.daemon = True
            self._isalive = True
            recibidor.start()

        except socket.error:
            print("No fue posible conectarse, revise la conexion")
            sys.exit()

    def recibir(self):
        while True:
            data = self.s_client.recv(2**28)
            print(len(data))
            if len(data) < 500:
                data = data.decode("utf-8")
                data = json.loads(data)
                print("Data: {}".format(data))
                if data["accion"] == "sala":
                    self.BE.set_salas(data["value"])
                elif data["accion"] == "chat_msg":
                    self.BE.set_chat(data["value"])
                elif data["accion"] == "comienzo_juego":
                    self.BE.empezar_juego(data["value"])
                elif data["accion"] == "cancion_recibida":
                    with open("Data/"+data["value"], "wb") as file:
                        file.write(self.bytes)
                    self.bytes = bytearray()
                elif data["accion"] == "user_info":
                    self.BE.puntos = data["value"]

            else:
                self.bytes.extend(data)

    def enviar_datos(self, datos):
        datos_a_enviar = json.dumps(datos)
        self.s_client.send(datos_a_enviar.encode("utf-8"))

    def disconnect(self):
        self._isalive = False
        msj = {"mensaje": "cliente desconectado"}
        self.enviar_datos(msj)

if __name__ == "__main__":
    usuario = str(input("> Ingrese Nombre Usuario"))
    cliente = Client()
    while True:
        inputing = input("[1] Mandar Mensaje\n [2] Desconectarse\n> ")
        if inputing == "1":
            texto = input("> ")
            cliente.enviar_datos({"mensaje": texto})
        elif inputing == "2":
            cliente.disconnect()
            break
