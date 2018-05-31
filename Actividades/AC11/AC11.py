import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import (QIcon, QPixmap)
import numpy as np
from PyQt5.QtCore import QSize
from PyQt5.QtTest import QTest


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_GUI()
        self.botones_apretados = []
        self.intentos = 0
        self.dados_vuelta = False
        self.botonocultar_apretado = False
        self.totales = 0

    def init_GUI(self):

        pixmap = QPixmap("Imgs/back.png")
        pixmap = pixmap.scaled(120,120)
        icon = QIcon(pixmap)

        # Creamos una etiqueta para status. Recordar que los os Widget simples
        # no tienen StatusBar.
        self.label1 = QLabel('intentos: ', self)
        self.label1.move(160,10)
        self.label2 = QLabel(' ', self)
        self.label2.move(250, 15)

        self.boton2 = QPushButton("Ocultar", self)
        self.boton2.move(360,15)
        self.boton2.clicked.connect(self.ocultar)
        # Creamos la grilla para ubicar los Widget (botones) de manera matricial
        self.grilla = QGridLayout()

        valores1 = ["1","2","3","4","5","6","7","8","9","10","11","12","b", "1","2","3","4","5","6","7","8","9","10","11","12"]
        self.valores = np.random.choice(valores1, 25, False)
        print(self.valores)


        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada boton guardados en la lista valores
        self.lista_botones = []
        posicion = [(i, j) for i in range(5) for j in range(5)]
        for posicion, valor in zip(posicion, self.valores):
            if valor == '':
                continue

            boton = QPushButton()
            boton.resize(90,90)
            boton.setIcon(icon)
            boton.setFixedHeight(90)
            boton.setFixedWidth(90)
            boton.setIconSize(QSize(90,90))
            boton.clicked.connect(self.boton_clickeado)
            self.lista_botones.append([posicion,valor])
            # El * permite convertir los elementos de la tupla como argumentos
            # independientes
            self.grilla.addWidget(boton, *posicion)

        # Creamos un layout vertical
        vbox = QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label1)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Programice')

    def ocultar(self):
        if len(self.botones_apretados) == 2:
            pixmap = QPixmap("Imgs/back.png")
            pixmap = pixmap.scaled(90, 90)
            icon = QIcon(pixmap)
            self.botones_apretados[0][0].setIcon(icon)
            self.botones_apretados[1][0].setIcon(icon)
            self.label2.hide()


    def boton_clickeado(self):
        if not self.dados_vuelta:
            self.label2.show()
            boton = self.sender()
            id = self.grilla.indexOf(boton)
            valor = self.lista_botones[id][1]
            pixmap = QPixmap("Imgs/{}.png".format(valor))
            pixmap = pixmap.scaled(90,90)
            icon = QIcon(pixmap)
            boton.setIcon(icon)
            boton.setIconSize(QSize(90,90))
            self.botones_apretados.append([boton, valor])

            if valor == "b":
                self.intentos += 10
                self.label1.setText("intentos: {}".format(self.intentos))
                self.label2.setText("3")
                QTest.qWait(1000)
                self.label2.setText("2")
                QTest.qWait(1000)
                self.label2.setText("1")
                QTest.qWait(1000)
                self.label2.setText("")
                pixmap = QPixmap("Imgs/back.png".format(valor))
                pixmap = pixmap.scaled(90, 90)
                icon = QIcon(pixmap)
                boton.setIcon(icon)
                self.botones_apretados = []

            if len(self.botones_apretados) == 2:
                self.dados_vuelta = True
                self.intentos += 1
                self.label1.setText("intentos : {}".format(self.intentos))

                if self.botones_apretados[0][1] != self.botones_apretados[1][1]:
                    if self.botones_apretados[1][1] == "b":
                        self.intentos += 10
                        self.label1.setText("intentos: {}".format(self.intentos))

                    self.label2.setText("3")
                    QTest.qWait(1000)
                    self.label2.setText("2")
                    QTest.qWait(1000)
                    self.label2.setText("1")
                    QTest.qWait(1000)
                    self.label2.setText("")
                    pixmap = QPixmap("Imgs/back.png".format(valor))
                    pixmap = pixmap.scaled(90, 90)
                    icon = QIcon(pixmap)
                    self.botones_apretados[0][0].setIcon(icon)
                    self.botones_apretados[1][0].setIcon(icon)
                    self.dados_vuelta = False
                    self.totales += 2
                    if self.totales == 24:
                        QMessageBox.warning(self, '', "Ganastes!!")

                self.dados_vuelta = False
                self.botones_apretados = []






if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())