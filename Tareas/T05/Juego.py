from PyQt5.QtWidgets import QLabel
from Elementos import *
from math import sqrt
class Game:
    def __init__(self,ventana, champion, nivel):
        self.ventana = ventana
        self.nivel = nivel
        self.minions = []
        self.minions_enemigo = []
        self.items = [champion]

    def run(self):
        minion = Minion(self.ventana, 300, 50)

    def additem(self,item):
        self.items.append(item)

    def checkproximity(self,one):
        prox = []
        for item in self.items:
            if one == item:
                continue
            elif abs(one.position[0] - item.position[0]) <= 200 and abs(one.position[1] - item.position[1]) <= 200:
                prox.append(item)
        return prox

