from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QGraphicsScene, QLabel, QPushButton, QGraphicsItem, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt, QTimer , pyqtSignal, QPoint
from PyQt5.QtTest import QTest
import sys
from Elementos import Champion, Inhibidor, Turret, Nexus, Champion_Enemigo, Minion
from Juego import Game
import Funciones
import Tienda
import time
import random

datos = uic.loadUiType("T05window/main1.ui")


class VentanaInicial(datos[0], datos[1]):
    cursorMove = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.angle = 20
        self.setMouseTracking(True)
        self.mousepos = [0,0]
        self.mouseposn = [0,0]
        self.label_3.move(0, 0)
        self.campeon1.hide()
        self.campeon2.hide()
        self.campeon3.hide()

        self.pushButton_3.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()

        self.pushButton.clicked.connect(self.click_button)
        self.campeon1.clicked.connect(self.click_button_2)
        self.campeon2.clicked.connect(self.click_button_2)
        self.campeon3.clicked.connect(self.click_button_2)
        self.pushButton_3.clicked.connect(self.click_button_3)

        self.setWindowTitle('League of Progra')

    def click_button(self):
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.label.setText("Elige tu campeon!")
        self.campeon1.show()
        pixmap1 = QPixmap("Img/maga/derecha.png")
        icon1 = QIcon(pixmap1)
        self.campeon1.setText("")
        self.campeon1.setIcon(icon1)
        self.campeon1.setIconSize(QSize(200, 200))
        self.campeon2.show()
        pixmap2 = QPixmap("Img/kina/abajo.png")
        icon2 = QIcon(pixmap2)
        self.campeon2.setText("")
        self.campeon2.setIcon(icon2)
        self.campeon2.setIconSize(QSize(200, 200))
        pixmap3 = QPixmap("Img/campeon_3/abajo.png")
        icon3 = QIcon(pixmap3)
        self.campeon3.setText("")
        self.campeon3.setIcon(icon3)
        self.campeon3.setIconSize(QSize(200, 200))
        self.campeon3.show()

    def click_button_2(self):
        boton = self.sender()
        if boton == self.campeon1:
            self.campeon_n = "maga"
        elif boton == self.campeon2:
            self.campeon_n = "kina"
        else:
            self.campeon_n = "campeon_3"

        self.campeon1.hide()
        self.campeon2.hide()
        self.campeon3.hide()
        self.label.setText("Estas Listo?!")
        self.pushButton_3.show()

    def click_button_3(self):
        self.nivel = random.choice(["Noob", "Normal", "RageQuitter"])
        self.start_game()

    def start_game(self):
        self.pantalla = QLabel("", self)
        self.pantalla.move(0, 0)
        self.pantalla.resize(self.width(), self.height())
        self.pantalla.show()
        self.pantalla.setMouseTracking(True)
        self.setMouseTracking(True)
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.pushButton_3.hide()
        self.label.hide()

        pixmap4 = QPixmap("Img/floor.png")
        pixmap4 = pixmap4.scaled(self.width(), self.height())
        self.label_3.resize(self.width(), self.height())
        self.label_3.setPixmap(pixmap4)
        self.label_3.setMouseTracking(True)


        # campeon usuario
        self.campeon = Champion(self.campeon_n, self, 30, 250)
        self.campeon.image.setMouseTracking(True)
        self.juego = Game(self, self.campeon, self.nivel)

        # campeon enemigo
        self.campeon_enemigo = Champion_Enemigo(self, 700, 300)
        self.juego.items.append(self.campeon_enemigo)

        # Nexus Amigo
        self.nexus = Nexus(1, self, 30, 30)
        self.juego.additem(self.nexus)
        self.nexus.image.setMouseTracking(True)

        # Inhibidor Amigo
        self.inhibidor = Inhibidor(1, self, 100, 100)
        self.juego.additem(self.inhibidor)
        self.inhibidor.image.setMouseTracking(True)

        # Torre Amiga
        self.torre = Turret(1, self, 180, 150, 1)
        self.torre.image.setMouseTracking(True)
        self.juego.items.append(self.torre)

        # Tienda

        self.tienda = Tienda.Tienda_BE(self)
        self.tienda_bt = QPushButton("", self)
        self.tienda_bt.move(self.tienda.posx, self.tienda.posy)
        pixmap_tienda = QPixmap("Img/misc/Chest.png")
        pixmap_tienda = pixmap_tienda.scaled(50,50)
        icon_tienda = QIcon(pixmap_tienda)
        self.tienda_bt.resize(50, 50)
        self.tienda_bt.setIcon(icon_tienda)
        self.tienda_bt.setIconSize(QSize(60,60))
        self.tienda_bt.show()
        self.tienda_bt.clicked.connect(self.tienda_pressed)
        self.tienda_bt.setMouseTracking(True)

        # Torre Enemiga
        self.torre2 = Turret(2, self, 710, 350, 2)
        self.torre2.image.setMouseTracking(True)
        self.juego.items.append(self.torre2)

        # Inhibidor Enemigo
        self.inhibidor2 = Inhibidor(2, self, 800, 430)
        self.juego.additem(self.inhibidor2)
        self.inhibidor2.image.setMouseTracking(True)


        # Nexus Enemigo
        self.nexus2 = Nexus(2, self, 900, 480)
        self.nexus2.image.setMouseTracking(True)
        self.juego.additem(self.nexus2)

        self.nexus.start()
        self.nexus2.start()
        self.inhibidor.start()
        self.inhibidor2.start()
        self.campeon_enemigo.start()
        self.torre2.start()
        self.torre.start()
        self.campeon.start()
        self.setMouseTracking(True)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_D:
            self.campeon.point = None

            if self.campeon.direccion == "arriba":
                self.campeon.position[0] += 5
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba2)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)


            elif self.campeon.direccion == "abajo":
                self.campeon.position[0] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo2)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)

            elif self.campeon.direccion == "derecha":
                self.campeon.position[1] += 5
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha2)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)

            elif self.campeon.direccion == "izq":
                self.campeon.position[1] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmapizq)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq2)
                self.campeon.image.setPixmap(self.campeon.pixmapizq)

            elif self.campeon.direccion == "diag1":
                self.campeon.position[1] += 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag11)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag12)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)

            elif self.campeon.direccion == "diag2":
                self.campeon.position[1] -= 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag21)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag22)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)

            elif self.campeon.direccion == "diag3":
                self.campeon.position[1] -= 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag31)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag32)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)

            elif self.campeon.direccion == "diag4":
                self.campeon.position[1] += 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag41)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag42)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)
        elif event.key() == Qt.Key_A:
            self.campeon.point = None
            if self.campeon.direccion == "arriba":
                self.campeon.position[0] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba2)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)


            elif self.campeon.direccion == "abajo":
                self.campeon.position[0] += self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo2)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)

            elif self.campeon.direccion == "derecha":
                self.campeon.position[1] -= self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha2)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)

            elif self.campeon.direccion == "izq":
                self.campeon.position[1] += self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapizq)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq2)
                self.campeon.image.setPixmap(self.campeon.pixmapizq)

            elif self.campeon.direccion == "diag1":
                self.campeon.position[1] -= self.campeon.velocidad * 0.03
                self.campeon.position[0] -= self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag11)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag12)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)

            elif self.campeon.direccion == "diag2":
                self.campeon.position[1] += self.campeon.velocidad * 0.03
                self.campeon.position[0] -= self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag21)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag22)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)

            elif self.campeon.direccion == "diag3":
                self.campeon.position[1] += self.campeon.velocidad * 0.03
                self.campeon.position[0] += self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag31)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag32)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)

            elif self.campeon.direccion == "diag4":
                self.campeon.position[1] -= self.campeon.velocidad * 0.03
                self.campeon.position[0] += self.campeon.velocidad * 0.03
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag41)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag42)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)



        elif event.key() == Qt.Key_W:
            self.campeon.point = None
            if self.campeon.direccion == "arriba":
                self.campeon.position[1] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba2)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)


            elif self.campeon.direccion == "abajo":
                self.campeon.position[1] += 5
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo2)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)

            elif self.campeon.direccion == "derecha":
                self.campeon.position[0] += 5
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha2)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)

            elif self.campeon.direccion == "izq":
                self.campeon.position[0] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmapizq)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq2)
                self.campeon.image.setPixmap(self.campeon.pixmapizq)

            elif self.campeon.direccion == "diag1":
                self.campeon.position[1] -= 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag11)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag12)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)

            elif self.campeon.direccion == "diag2":
                self.campeon.position[1] -= 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag21)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag22)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)

            elif self.campeon.direccion == "diag3":
                self.campeon.position[1] += 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag31)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag32)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)

            elif self.campeon.direccion == "diag4":
                self.campeon.position[1] += 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag41)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag42)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)


        elif event.key() == Qt.Key_S:
            self.campeon.point = None
            if self.campeon.direccion == "arriba":
                self.campeon.position[1] += 5
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba2)
                self.campeon.image.setPixmap(self.campeon.pixmaparriba)


            elif self.campeon.direccion == "abajo":
                self.campeon.position[1] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo2)
                self.campeon.image.setPixmap(self.campeon.pixmapabajo)

            elif self.campeon.direccion == "derecha":
                self.campeon.position[0] -= 5
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha2)
                self.campeon.image.setPixmap(self.campeon.pixmapderecha)

            elif self.campeon.direccion == "izq":
                self.campeon.position[0] += 5
                self.campeon.image.setPixmap(self.campeon.pixmapizq)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq1)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapizq2)
                self.campeon.image.setPixmap(self.campeon.pixmapizq)

            elif self.campeon.direccion == "diag1":
                self.campeon.position[1] += 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag11)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag12)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag10)

            elif self.campeon.direccion == "diag2":
                self.campeon.position[1] += 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag21)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag22)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag20)

            elif self.campeon.direccion == "diag3":
                self.campeon.position[1] -= 3
                self.campeon.position[0] += 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag31)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag32)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag30)

            elif self.campeon.direccion == "diag4":
                self.campeon.position[1] -= 3
                self.campeon.position[0] -= 3
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag41)
                QTest.qWait(30)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag42)
                self.campeon.image.setPixmap(self.campeon.pixmapdiag40)

    def mousePressEvent(self, event):
        point = [event.pos().x(), event.pos().y()]
        for item in self.juego.items:
            x = item.position[0]
            y = item.position[1]
            if x <= point[0] <= 60+x and y <= point[1] <= 60+y and item.equipo != 1:
                self.campeon.point = point
            else:
                pass

    def tienda_pressed(self):
        if self.campeon.position[0] - self.tienda.posx < 100 and self.campeon.position[1] - self.tienda.posy < 100:

            ventana_tienda = QDialog(self)
            ventana_tienda.resize(700, 350)
            titulo = QLabel("Bienvenido a la tienda!", ventana_tienda)
            titulo.move(180, 20)
            titulo.show()

            label1 = QLabel("Puntos Disponibles : {}".format(self.campeon.puntos), ventana_tienda)
            label1.move(500, 30)
            label1.show()
            boton_tienda_1 = QPushButton("Arma de Mano", ventana_tienda)
            boton_tienda_1.move(20, 50)
            label_boton_1 = QLabel("Precio = {}\nAtributo = {}".format(self.tienda.objetos_disponibles["Arma de mano"].precio, self.tienda.objetos_disponibles["Arma de mano"].atributo[1]), ventana_tienda)
            label_boton_1.move(20, 80)
            label_boton_1.show()
            boton_tienda_1.show()

            boton_tienda_2 = QPushButton("Arma de distancia", ventana_tienda)
            boton_tienda_2.move(220, 50)
            label_boton_2 = QLabel("Precio = {}\nAtributo = {}".format
                                   (self.tienda.objetos_disponibles["Arma de distancia"].precio, self.tienda.objetos_disponibles["Arma de distancia"].atributo[1]), ventana_tienda)
            label_boton_2.move(220, 80)
            label_boton_2.show()
            boton_tienda_2.show()

            boton_tienda_3 = QPushButton("Botas", ventana_tienda)
            boton_tienda_3.move(420, 50)
            label_boton_3 = QLabel("Precio ={} \nAtributo ={}".format(self.tienda.objetos_disponibles["Botas"].precio, self.tienda.objetos_disponibles["Botas"].atributo[1]), ventana_tienda)
            label_boton_3.move(420, 80)
            label_boton_3.show()
            boton_tienda_3.show()

            boton_tienda_4 = QPushButton("Baculo", ventana_tienda)
            boton_tienda_4.move(20, 250)
            label_boton_4 = QLabel("Precio = {}\nAtributo = {}".format(self.tienda.objetos_disponibles["Baculo"].precio, self.tienda.objetos_disponibles["Baculo"].atributo[1]), ventana_tienda)
            label_boton_4.move(20, 280)
            label_boton_4.show()
            boton_tienda_4.show()

            boton_tienda_5 = QPushButton("Armadura", ventana_tienda)
            boton_tienda_5.move(220, 250)
            label_boton_5 = QLabel("Precio = {}\nAtributo = {}".format(self.tienda.objetos_disponibles["Armadura"].precio, self.tienda.objetos_disponibles["Armadura"].atributo[1]), ventana_tienda)
            label_boton_5.move(220, 280)
            label_boton_5.show()
            boton_tienda_5.show()

            boton_tienda_6 = QPushButton("Carta Earthstone", ventana_tienda)
            boton_tienda_6.move(420, 250)
            label_boton_6 = QLabel("Precio = {}\nAtributo = {}".format(self.tienda.objetos_disponibles["Carta Hearthstone"].precio, self.tienda.objetos_disponibles["Carta Hearthstone"].atributo[1]), ventana_tienda)
            label_boton_6.move(420, 280)
            label_boton_6.show()
            boton_tienda_6.show()

            ventana_tienda.show()

            boton_tienda_1.clicked.connect(self.comprar_tienda)
            boton_tienda_2.clicked.connect(self.comprar_tienda)
            boton_tienda_3.clicked.connect(self.comprar_tienda)
            boton_tienda_4.clicked.connect(self.comprar_tienda)
            boton_tienda_5.clicked.connect(self.comprar_tienda)
            boton_tienda_6.clicked.connect(self.comprar_tienda)

        else:
            QMessageBox.warning(self, "", "Debes acercarte a la tienda!")

    def comprar_tienda(self):
        boton = self.sender()
        text = boton.text()

        if text == "Botas":
            self.tienda.comprar_botas()
        elif text == "Armadura":
            self.tienda.comprar_armadura()
        elif text == "Arma de Mano":
            self.tienda.comprar_arma_mano()
        elif text == "Arma de distancia":
            self.tienda.comprar_arma_distancia()
        elif text == "Baculo":
            self.tienda.comprar_baculo()
        else:
            self.tienda.comprar_hearthstone()

    @staticmethod
    def actualizar_imagen(myImageEvent):
        label = myImageEvent.image
        label.move(myImageEvent.x, myImageEvent.y)
        vida = myImageEvent.vida
        vida.setValue(myImageEvent.health)

    def mouseMoveEvent(self, event):
        self.mousepos = [int(event.pos().x()), int(event.pos().y())]

        self.campeon.direccion = Funciones.direccion(self.campeon.position, self.mousepos)

        if self.campeon.direccion == "arriba":
            self.campeon.image.setPixmap(self.campeon.pixmaparriba)
        elif self.campeon.direccion == "abajo":
            self.campeon.image.setPixmap(self.campeon.pixmapabajo)
        elif self.campeon.direccion == "derecha":
            self.campeon.image.setPixmap(self.campeon.pixmapderecha)
        elif self.campeon.direccion == "izq":
            self.campeon.image.setPixmap(self.campeon.pixmapizq)
        elif self.campeon.direccion == "diag1":
            self.campeon.image.setPixmap(self.campeon.pixmapdiag10)
        elif self.campeon.direccion == "diag2":
            self.campeon.image.setPixmap(self.campeon.pixmapdiag20)
        elif self.campeon.direccion == "diag3":
            self.campeon.image.setPixmap(self.campeon.pixmapdiag30)
        elif self.campeon.direccion == "diag4":
            self.campeon.image.setPixmap(self.campeon.pixmapdiag40)



if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    fond = VentanaInicial()
    fond.show()
    sys.exit(app.exec())