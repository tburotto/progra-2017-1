from PyQt5.QtGui import QPixmap
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QLabel, QProgressBar
import random
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import time
from Funciones import checkdistance

class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """

    def __init__(self, image, x, y, vida, health):
        self.image = image
        self.x = x
        self.y = y
        self.vida = vida
        self.health = health


class Minion(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self, parent, x, y, equipo):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.resistencia = 0
        self.health = 45
        self.dano = 2
        self.distancia = 5
        self.velocidad = 8
        self.equipo = equipo
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(40,40)
        if self.equipo == 1:
            self.image.setPixmap(QPixmap("Img/misc/minion.png").scaled(40,40))
        else:
            self.image.setPixmap(QPixmap("Img/misc/minion1.png").scaled(40, 40))
        self.image.show()
        self.image.setVisible(True)
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60,5)
        self.vida.show()
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]
        self.destination = False

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1],self.vida,self.health))

        self.trigger.emit(MoveMyImageEvent(
            self.vida, self.position[0]+10, self.position[1]-5,
        self.vida, self.health))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        self.vida.setValue(self.health)
        while self.health > 0:
            time.sleep(0.3)
            if self.destination == False:
                if self.equipo == 1:
                    self.position = [self.position[0] + random.randint(0, 10), self.position[1] + random.randint(0, 5)]
                else:
                    self.position = [self.position[0] - random.randint(0, 10), self.position[1] - random.randint(0, 5)]
            proximity = self.parent.juego.checkproximity(self)
            if len(proximity) != 0:
                for item in proximity:
                    if item.equipo != self.equipo:
                        self.destination = True
                        if abs(self.position[0] - item.position[0]) > self.distancia:
                            if self.position[0] > item.position[0]:
                                self.position = [self.position[0] - random.randint(1, 10), self.position[1]]
                            else:
                                self.position = [self.position[0] + random.randint(1, 10), self.position[1]]

                        if abs(self.position[1] - item.position[1]) > self.distancia:
                            if self.position[1] > item.position[1]:
                                self.position = [self.position[0], self.position[1] - random.randint(1, 10)]
                            else:
                                self.position = [self.position[0], self.position[1] + random.randint(1, 10)]
                        else:
                            self.atacar(item)
                    else:
                        self.destination = False
            else:
                self.destination = False

        self.image.hide()
        self.parent.juego.items.remove(self)
        self.vida.hide()

    def atacar(self, item):
        if checkdistance(self, item) < self.distancia:
            item.health -= self.dano - item.resistencia


class Champion(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self,name, parent, x, y):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.name = name
        self.cm = 0
        if self.name == "maga":
            self.velocidad = 30
            self.distancia = 40
            self.resistencia = 0
            self.dano = 10
            self.health = 500
        elif self.name == "kina":
            self.dano = 20
            self.velocidad = 10
            self.distancia = 5
            self.resistencia = 0
            self.health = 666
        else:
            self.dano = 15
            self.velocidad = 20
            self.distancia = 50
            self.resistencia = 0
            self.health = 300

        self.puntos = 0
        self.equipo = 1
        self.image = QLabel(parent)
        self.parent = parent
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60,5)
        self.vida.show()
        self.image.resize(60,60)
        self.image.setPixmap(QPixmap("Img/"+str(name)+"/derecha.png").scaled(60,60))
        self.pixmap = QPixmap("Img/"+str(name)+"/derecha.png").scaled(60,60)

        self.direccion = "derecha"

        self.pixmapderecha = QPixmap("Img/" + str(name) + "/derecha.png").scaled(60,60)
        self.pixmapderecha1 = QPixmap("Img/" + str(name) + "/derecha1.png").scaled(60, 60)
        self.pixmapderecha2 = QPixmap("Img/" + str(name) + "/derecha2.png").scaled(60, 60)

        self.pixmapizq = QPixmap("Img/" + str(name) + "/izquierda.png").scaled(60,60)
        self.pixmapizq1 = QPixmap("Img/" + str(name) + "/izquierda1.png").scaled(60, 60)
        self.pixmapizq2 = QPixmap("Img/" + str(name) + "/izquierda2.png").scaled(60, 60)

        self.pixmaparriba = QPixmap("Img/" + str(name) + "/arriba.png").scaled(60,60)
        self.pixmaparriba1 = QPixmap("Img/" + str(name) + "/arriba1.png").scaled(60, 60)
        self.pixmaparriba2 = QPixmap("Img/" + str(name) + "/arriba2.png").scaled(60, 60)

        self.pixmapabajo = QPixmap("Img/" + str(name) + "/abajo.png").scaled(60,60)
        self.pixmapabajo1 = QPixmap("Img/" + str(name) + "/abajo1.png").scaled(60, 60)
        self.pixmapabajo2 = QPixmap("Img/" + str(name) + "/abajo2.png").scaled(60, 60)

        self.pixmapdiag10 = QPixmap("Img/" + str(name) + "/diag10.png").scaled(60, 60)
        self.pixmapdiag11 = QPixmap("Img/" + str(name) + "/diag11.png").scaled(60, 60)
        self.pixmapdiag12 = QPixmap("Img/" + str(name) + "/diag12.png").scaled(60, 60)

        self.pixmapdiag20 = QPixmap("Img/" + str(name) + "/diag20.png").scaled(60, 60)
        self.pixmapdiag21 = QPixmap("Img/" + str(name) + "/diag21.png").scaled(60, 60)
        self.pixmapdiag22 = QPixmap("Img/" + str(name) + "/diag22.png").scaled(60, 60)

        self.pixmapdiag30 = QPixmap("Img/" + str(name) + "/diag30.png").scaled(60, 60)
        self.pixmapdiag31 = QPixmap("Img/" + str(name) + "/diag31.png").scaled(60, 60)
        self.pixmapdiag32 = QPixmap("Img/" + str(name) + "/diag32.png").scaled(60, 60)

        self.pixmapdiag40 = QPixmap("Img/" + str(name) + "/diag40.png").scaled(60, 60)
        self.pixmapdiag41 = QPixmap("Img/" + str(name) + "/diag41.png").scaled(60, 60)
        self.pixmapdiag42 = QPixmap("Img/" + str(name) + "/diag42.png").scaled(60, 60)

        self.image.show()
        self.vida.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.vida.setValue(self.health)
        self.position = [x, y]
        self.point = None

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1], self.vida, self.health))

        self.trigger.emit(MoveMyImageEvent(
            self.vida, self.position[0] +10, self.position[1] -10, self.vida, self.health))


    def run(self):
        self.vida.setValue(self.health)
        while self.health > 0:
            time.sleep(0.03)
            if self.point != None:
                m = (self.position[1]- self.point[1])/(self.position[0]-self.point[0])
                if self.point[0] > self.position[0] and self.point[1] > self.position[1]:
                    if abs(self.position[0] - self.point[0]) > self.distancia and abs(self.position[1] - self.point[1]) > self.distancia:
                        time.sleep(0.01)
                        self.position[0] += self.velocidad *0.03
                        self.position[1] += self.velocidad*m *0.03
                    else:
                        for item in self.parent.juego.items:
                            if abs(self.position[0] - item.position[0]) > self.distancia and abs(self.position[1] - item.position[1]) > self.distancia:
                                try:
                                    self.atacar(item)
                                except ValueError:
                                    self.point = None
                                    if isinstance(item, Minion) or isinstance(item, SuperMinion):
                                        self.puntos += 1
                                    elif isinstance(item, Champion_Enemigo):
                                        self.puntos += 5
                                    elif isinstance(item, Turret):
                                        self.puntos += 15
                elif self.point[0] < self.position[0] and self.point[1] < self.position[1]:
                    if abs(self.position[0] - self.point[0]) > self.distancia and abs(self.position[1] - self.point[1]) > self.distancia:
                        time.sleep(0.01)
                        self.position[0] -= self.velocidad *0.03
                        self.position[1] -= self.velocidad*m *0.03
                    else:
                        for item in self.parent.juego.items:
                            if abs(self.position[0] - item.position[0]) > self.distancia and abs(self.position[1] - item.position[1]) > self.distancia:
                                try:
                                    self.atacar(item)
                                except ValueError:
                                    self.point = None
                                    if isinstance(item, Minion) or isinstance(item, SuperMinion):
                                        self.puntos += 1
                                    elif isinstance(item, Champion_Enemigo):
                                        self.puntos += 5
                                    elif isinstance(item, Turret):
                                        self.puntos += 15

                elif self.point[0] < self.position[0] and self.point[1] > self.position[1]:
                    if abs(self.position[0] - self.point[0]) > self.distancia and abs(
                                    self.position[1] - self.point[1]) > self.distancia:
                        time.sleep(0.01)
                        self.position[0] -= self.velocidad *0.03
                        self.position[1] += self.velocidad * m *0.03
                    else:
                        for item in self.parent.juego.items:
                            if abs(self.position[0] - item.position[0]) > self.distancia and abs(self.position[1] - item.position[1]) > self.distancia:
                                try:
                                    self.atacar(item)
                                except ValueError:
                                    self.point = None
                                    if isinstance(item, Minion) or isinstance(item, SuperMinion):
                                        self.puntos += 1
                                    elif isinstance(item, Champion_Enemigo):
                                        self.puntos += 5
                                    elif isinstance(item, Turret):
                                        self.puntos += 15
                elif self.point[0] > self.position[0] and self.point[1] < self.position[1]:
                    if abs(self.position[0] - self.point[0]) > self.distancia and abs(
                                    self.position[1] - self.point[1]) > self.distancia:
                        time.sleep(0.01)
                        self.position[0] += self.velocidad *0.03
                        self.position[1] -= self.velocidad * m *0.03
                    else:
                        for item in self.parent.juego.items:
                            if abs(self.position[0] - item.position[0]) > self.distancia and abs(self.position[1] - item.position[1]) > self.distancia:
                                try:
                                    self.atacar(item)
                                except ValueError:
                                    self.point = None
                                    if isinstance(item, Minion) or isinstance(item, SuperMinion):
                                        self.puntos += 1
                                    elif isinstance(item, Champion_Enemigo):
                                        self.puntos += 5
                                    elif isinstance(item, Turret):
                                        self.puntos += 15

            self.position = [self.position[0], self.position[1]]

        print("Estas Muerto!")
        self.cm += 1
        self.tiempo = (1.1**self.cm)*10
        self.vida.hide()
        self.image.hide()
        self.parent.juego.items.remove(self)
        QTest.qWait(self.tiempo)
        self.position = [30, 250]
        self.image.show()
        self.parent.juego.items.append(self)
        self.start()

    def move_to(self, point):
        if point[0] > self.position[0] and point[1] < self.position[1]:
            print("aca")
            m = point[1]/point[0]
            while abs(self.position[0] - point[0]) > 20 and abs(self.position[1] - point[1]) > 20:
                time.sleep(0.01)
                self.position[0] += 2
                self.position[1] -= m*2

            self.point = None
    def atacar(self, item):
        if checkdistance(self, item) < self.distancia:
            item.health -= self.dano

class Inhibidor(QTimer):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv
    def __init__(self,equipo, parent, x, y):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.health = 600
        self.equipo = equipo
        self.resistencia = 0
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(100,100)
        self.image.setPixmap(QPixmap("Img/misc/inhibitor.png").scaled(100, 100))
        self.image.show()
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60, 5)
        self.vida.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]
        self.timeout.connect(self.minions)
        self.start(10000)
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1],
        self.vida, self.health))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])
    def run(self):
        while self.health > 0:
            pass
        self.image.hide()
        self.parent.juego.items.remove(self)

    def minions(self):
            if self.equipo == 1:
                for i in range(1, 4):
                    minion = Minion(self.parent, self.position[0]+100+random.randint(1,5), self.position[1]+100+random.randint(1,5), self.equipo)
                    minion.start()
                    self.parent.juego.additem(minion)
                super = SuperMinion(self.parent, self.position[0]+100+random.randint(1,5), self.position[1]+100+random.randint(1,5), self.equipo)
                super.start()
                self.parent.juego.additem(super)
            else:
                for i in range(1, 4):
                    minion = Minion(self.parent, self.position[0]-100-random.randint(1,5), self.position[1]-100-random.randint(1,5), self.equipo)
                    minion.start()
                    self.parent.juego.additem(minion)
                super = SuperMinion(self.parent, self.position[0]-100-random.randint(1,5), self.position[1]-100-random.randint(1,5), self.equipo)
                super.start()
                self.parent.juego.additem(super)



class Turret(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self,name, parent, x, y, equipo):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.health = 250
        self.equipo = equipo
        self.name = name
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(100,100)
        self.resistencia = 0
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60,5)
        self.vida.show()

        if self.name == 1:
            self.image.setPixmap(QPixmap("Img/misc/turret1.png").scaled(100, 100))
        else:
            self.image.setPixmap(QPixmap("Img/misc/turret.png").scaled(100, 100))
        self.image.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1], self.vida, self.health
        ))

        self.trigger.emit(MoveMyImageEvent(
            self.vida, self.position[0] + 10, self.position[1] - 5, self.vida, self.health
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        self.vida.setValue(self.health)
        while self.health > 0:
            proximity = self.parent.juego.checkproximity(self)
            if len(proximity) != 0:
                for item in proximity:
                    if item.equipo != self.name and checkdistance(self, item) <= 40:
                        QTest.qWait(1000)
                        self.attack(item)

        self.image.hide()
        self.vida.hide()
        self.parent.juego.items.remove(self)

    def attack(self, item):
        for a in self.parent.juego.items:
            if a == item:
                a.health -= 30


class Champion_Enemigo(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self, parent, x, y):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.health = 500
        self.resistencia = 0
        self.equipo = 2
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(60, 60)
        champion = random.choice(["maga", "kina"])
        if champion == "maga":
            self.image.setPixmap(QPixmap("Img/maga/izquierda.png").scaled(60, 60))
        elif champion == "kina":
            self.image.setPixmap(QPixmap("Img/kina/izquierda.png").scaled(60, 60))
        self.image.show()

        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60,5)
        self.vida.show()

        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]
        self.destination = False

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1],self.vida, self.health
        ))

        self.trigger.emit(MoveMyImageEvent(
            self.vida, self.position[0] + 10, self.position[1]-5,self.vida, self.health
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        self.vida.setValue(self.health)
        QTest.qWait(10000)
        while self.health > 0:
            time.sleep(0.3)
            if self.destination == False:
                self.position = [self.position[0]-random.randint(0,10), self.position[1]-random.randint(0,5)]
            proximity = self.parent.juego.checkproximity(self)
            if len(proximity) != 0:
                for item in proximity:
                    if item.equipo != self.equipo:
                        self.destination = True
                        if abs(self.position[0] - item.position[0]) > 20:
                            if self.position[0] > item.position[0]:
                                self.position = [self.position[0] - random.randint(1,10), self.position[1]]
                            else:
                                self.position = [self.position[0] + random.randint(1, 10), self.position[1]]

                        if abs(self.position[1] - item.position[1]) > 20:
                            if self.position[1] > item.position[1]:
                                self.position = [self.position[0], self.position[1] - random.randint(1,10)]
                            else:
                                self.position = [self.position[0], self.position[1] + random.randint(1, 10)]
                        else:
                            self.atacar(item)
                    else:
                        self.destination = False
            else:
                self.destination = False

        self.vida.hide()
        self.image.hide()
        self.parent.juego.items.remove(self)


    def atacar(self, item):
        if checkdistance(self, item) < 60:
            item.health -= 10


class SuperMinion(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self, parent, x, y, equipo):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.health = 60
        self.dano = 4
        self.distancia = 20
        self.resistencia = 0
        self.equipo = equipo
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(40,40)
        if self.equipo == 1:
            self.image.setPixmap(QPixmap("Img/misc/miniong.png").scaled(40,40))
        else:
            self.image.setPixmap(QPixmap("Img/misc/miniong1.png").scaled(40, 40))
        self.image.show()
        self.image.setVisible(True)
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60,5)
        self.vida.show()
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]
        self.destination = False

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1],self.vida, self.health
        ))
        self.trigger.emit(MoveMyImageEvent(
            self.vida, self.position[0]+10, self.position[1]-5,self.vida, self.health
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        self.vida.setValue(self.health)
        while self.health > 0:
            time.sleep(0.3)
            if self.destination == False:
                if self.equipo == 1:
                    self.position = [self.position[0] + random.randint(0, 10), self.position[1] + random.randint(0, 5)]
                else:
                    self.position = [self.position[0] - random.randint(0, 10), self.position[1] - random.randint(0, 5)]
            proximity = self.parent.juego.checkproximity(self)
            if len(proximity) != 0:
                for item in proximity:
                    if item.equipo != self.equipo:
                        self.destination = True
                        if abs(self.position[0] - item.position[0]) > 20:
                            if self.position[0] > item.position[0]:
                                self.position = [self.position[0] - random.randint(1, 10), self.position[1]]
                            else:
                                self.position = [self.position[0] + random.randint(1, 10), self.position[1]]

                        if abs(self.position[1] - item.position[1]) > 20:
                            if self.position[1] > item.position[1]:
                                self.position = [self.position[0], self.position[1] - random.randint(1, 10)]
                            else:
                                self.position = [self.position[0], self.position[1] + random.randint(1, 10)]
                        else:
                            self.atacar(item)
                    else:
                        self.destination = False
            else:
                self.destination = False

        self.image.hide()
        self.parent.juego.items.remove(self)
        self.vida.hide()



    def atacar(self, item):
        if checkdistance(self, item) < 60:
            item.health -= self.dano

class Nexus(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv
    def __init__(self,equipo, parent, x, y):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.health = 1200
        self.equipo = equipo
        self.resistencia = 0
        self.image = QLabel(parent)
        self.parent = parent
        self.image.resize(100,100)
        self.image.setPixmap(QPixmap("Img/misc/nexus.png").scaled(100, 100))
        self.image.show()
        self.vida = QProgressBar(parent)
        self.vida.setMaximum(self.health)
        self.vida.setMinimum(0)
        self.vida.resize(60, 5)
        self.vida.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = [x, y]
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1],
        self.vida, self.health))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])
    def run(self):
        self.vida.setValue(self.health)
        while self.health > 0:
            pass
        self.image.hide()


