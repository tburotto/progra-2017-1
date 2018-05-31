import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QListWidget
from PyQt5.QtMultimedia import QSound
from PyQt5.QtTest import QTest
from PyQt5.QtGui import QFont
import BE_Client
import time

DATA = uic.loadUiType("ventana.ui")


class MainWindow(DATA[0], DATA[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollArea.hide()
        self.label_6.hide()
        self.pushButton.clicked.connect(self.iniciar_sesion)
        self.setWindowTitle("PrograPop")
        self.scrollArea_2.hide()
        self.label_tiempo = QLabel("20", self)
        self.label_tiempo.move(500, 300)
        self.label_tiempo.resize(100,100)
        self.label_tiempo.setFont(QFont("SansSerif", 20))
        self.label_tiempo.hide()
        self.song_name = None
        self.song = None
        self.salas = [{"name": "hola", "usuarios":[], "artistas": "None"}]
        self.a = 0
        self.chat = QListWidget(self)
        self.chat.resize(1000, 300)
        self.chat.move(30,370)
        self.chat.hide()


    def iniciar_sesion(self):
        self.name = self.lineEdit.text()
        self.usuario_back = BE_Client.Client_Back(self)
        time.sleep(2)
        self.usuario_back.get_salas()
        time.sleep(2)
        self.lineEdit.hide()
        self.label_2.hide()
        self.pushButton.hide()
        self.titulo.setText("Elige una Sala")

        self.lista_items = QListWidget(self)

        for item in self.salas:
            self.lista_items.addItem("Sala : {}, Usuarios: {}, artistas: {}".format(item["name"],
                                                                                    len(item["usuarios"]), item["artistas"]))

        self.lista_items.show()
        self.lista_items.resize(500,200)
        self.lista_items.move(300,200)

        self.lista_items.itemClicked.connect(self.conectarse_sala)
        self.actualizar = QPushButton("Actualizar", self)
        self.actualizar.move(1000, 100)
        self.actualizar.show()
        self.actualizar.clicked.connect(self.actualizar_salas)

    def conectarse_sala(self, item):
        self.lista_items.hide()
        name = item.text().split(",")[0].split(":")[1].replace(" ", "")

        self.sala_actual = name
        self.usuario_back.connect_sala(name)

        self.usuario_back.get_info()
        self.scrollArea.hide()
        self.titulo.setText(name)
        self.label_6.hide()
        self.actualizar.hide()
        self.volver = QPushButton("Salir", self)
        self.volver.move(30, 30)
        self.volver.clicked.connect(self.volver_menu)
        self.volver.show()

        # CHAT

        self.chat.show()
        self.chat.addItem("Chat")
        self.line_chat = QLineEdit(self)
        self.line_chat.move(40, 690)
        self.line_chat.resize(1000, 30)
        self.chatButton = QPushButton("Enviar", self)
        self.chatButton.move(1050, 690)
        self.chatButton.show()
        self.line_chat.show()
        self.chatButton.clicked.connect(self.enviar_mensaje)

        # Juego
        self.opcion1 = QPushButton("opcion1", self)
        self.opcion2 = QPushButton("opcion2", self)
        self.opcion3 = QPushButton("opcion3 ", self)

        self.opcion1.move(30, 200)
        self.opcion2.move(400, 200)
        self.opcion3.move(700, 200)

        self.opcion1.resize(200,30)
        self.opcion2.resize(200, 30)
        self.opcion3.resize(200, 30)

        self.opcion1.show()
        self.opcion2.show()
        self.opcion3.show()

        self.opcion1.clicked.connect(self.opcion_selecta)
        self.opcion2.clicked.connect(self.opcion_selecta)
        self.opcion3.clicked.connect(self.opcion_selecta)

        while self.sala_actual != None:
            while not self.song_name:
                pass
            self.song = QSound(self.song_name)
            self.song_name = None
            self.song.play()
            self.label_tiempo.show()
            self.opcion1.show()
            self.opcion2.show()
            self.opcion3.show()
            QTest.qWait(1000)
            QTest.qWait(1000)
            self.label_tiempo.setText("19")
            QTest.qWait(1000)
            self.label_tiempo.setText("19")
            QTest.qWait(1000)
            self.label_tiempo.setText("17")
            QTest.qWait(1000)
            self.label_tiempo.setText("16")
            QTest.qWait(1000)
            self.label_tiempo.setText("15")
            QTest.qWait(1000)
            self.label_tiempo.setText("14")
            QTest.qWait(1000)
            self.label_tiempo.setText("13")
            QTest.qWait(1000)
            self.label_tiempo.setText("12")
            QTest.qWait(1000)
            self.label_tiempo.setText("11")
            QTest.qWait(1000)
            self.label_tiempo.setText("10")
            QTest.qWait(1000)
            self.label_tiempo.setText("9")
            QTest.qWait(1000)
            self.label_tiempo.setText("8")
            QTest.qWait(1000)
            self.label_tiempo.setText("7")
            QTest.qWait(1000)
            self.label_tiempo.setText("6")
            QTest.qWait(1000)
            self.label_tiempo.setText("5")
            QTest.qWait(1000)
            self.label_tiempo.setText("4")
            QTest.qWait(1000)
            self.label_tiempo.setText("3")
            QTest.qWait(1000)
            self.label_tiempo.setText("2")
            QTest.qWait(1000)
            self.label_tiempo.setText("1")
            QTest.qWait(1000)
            self.opcion1.hide()
            self.opcion2.hide()
            self.opcion3.hide()
            self.label_tiempo.hide()
            self.label_tiempo.setText("20")
            self.chat.addItem("Server: Preparate para la siguiente ronda")
            self.song.stop()
            QTest.qWait(1000)

    def actualizar_salas(self):
        self.lista_items.clear()
        self.usuario_back.get_salas()
        for item in self.salas:
            self.lista_items.addItem("Sala : {}, Usuarios: {}, artistas: {}".format(item["name"],
                                                                                    len(item["usuarios"]),
                                                                                    item["artistas"]))

    def volver_menu(self):
        self.chat.clear()
        self.chat.hide()
        self.usuario_back.get_salas()
        time.sleep(0.2)
        self.usuario_back.disconnect_sala(self.sala_actual)
        time.sleep(0.2)
        self.usuario_back.get_info()
        time.sleep(0.2)
        self.sala_actual = None
        self.song.stop()
        self.titulo.setText("Elige una Sala")
        self.label_6.setText("Bienvenido {}\nTienes {} puntos".format(self.name, self.usuario_back.puntos))
        self.label_6.show()
        self.label.setText("Nombre: {} - Usuarios : {} - Artistas : {}"
                           .format(self.salas[0]["name"], len(self.salas[0]["usuarios"]), self.salas[0]["artistas"]))
        self.lista_items.show()
        self.actualizar.show()
        self.volver.hide()
        self.line_chat.hide()
        self.chatButton.hide()
        self.scrollArea_2.hide()

        self.opcion1.hide()
        self.opcion2.hide()
        self.opcion3.hide()

    def enviar_mensaje(self):
        mensaje = self.line_chat.text()
        self.line_chat.setText("")
        self.usuario_back.chat(mensaje, self.sala_actual)

    def opcion_selecta(self):
        boton = self.sender()
        self.opcion1.hide()
        self.opcion2.hide()
        self.opcion3.hide()
        self.usuario_back.desicion(boton.text())

if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
    if form.usuario_back:
        form.usuario_back.disconnect()
