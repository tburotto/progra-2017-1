from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import sys
import random
class Tienda_BE:
    def __init__(self, ventana):
        self.ventana = ventana
        self.posx = 20
        self.posy = 180
        self.objetos_disponibles = {"Arma de mano" : Objeto("Arma de mano", 5, ["dano", 2]),
                                    "Arma de distancia": Objeto(["Arma de distancia"], 5, ["distancia", 2]),
                                    "Baculo": Objeto("Baculo", 7, ["habilidad", 2]),
                                    "Armadura": Objeto("Armadura", 5, ["resitencia", 2]),
                                    "Carta Hearthstone": Objeto("Carta Hearthstone", 10, ["random", 6]),
                                    "Botas": Objeto("Botas", 3, ["velocidad", 2])}

    def comprar_botas(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Botas"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Botas"].precio
            self.ventana.campeon.velocidad += self.objetos_disponibles["Botas"].atributo[1]
            self.objetos_disponibles["Botas"].atributo[1] = round(self.objetos_disponibles["Botas"].atributo[1]*1.5)
            self.objetos_disponibles["Botas"].precio += self.objetos_disponibles["Botas"].precio/2
            print("Botas compradas!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")


    def comprar_arma_mano(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Arma de mano"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Arma de mano"].precio
            self.ventana.campeon.dano += self.objetos_disponibles["Arma de mano"].atributo[1]
            self.objetos_disponibles["Arma de mano"].atributo[1] = round(self.objetos_disponibles["Arma de mano"].atributo[1] * 1.5)
            self.objetos_disponibles["Arma de mano"].precio += self.objetos_disponibles["Arma de mano"].precio / 2
            print("Arma de mano comprada!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")

    def comprar_arma_distancia(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Arma de distancia"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Arma de distancia"].precio
            self.ventana.campeon.distancia += self.objetos_disponibles["Arma de distancia"].atributo[1]
            self.objetos_disponibles["Arma de distancia"].atributo[1] = round(self.objetos_disponibles["Arma de distancia"].atributo[1] * 1.5)
            self.objetos_disponibles["Arma de distancia"].precio += self.objetos_disponibles["Arma de distancia"].precio / 2
            print("Arma de distancia comprada!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")

    def comprar_baculo(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Baculo"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Baculo"].precio
            self.ventana.campeon.habilidad += self.objetos_disponibles["Baculo"].atributo[1]
            self.objetos_disponibles["Baculo"].atributo[1] = round(self.objetos_disponibles["Baculo"].atributo[1] * 1.5)
            self.objetos_disponibles["Baculo"].precio += self.objetos_disponibles["Baculo"].precio / 2
            print("Baculo comprado!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")

    def comprar_armadura(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Armadura"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Armadura"].precio
            self.ventana.campeon.resistencia += self.objetos_disponibles["Armadura"].atributo[1]
            self.objetos_disponibles["Armadura"].atributo[1] = round(self.objetos_disponibles["Armadura"].atributo[1] * 1.5)
            self.objetos_disponibles["Armadura"].precio += self.objetos_disponibles["Armadura"].precio / 2
            print("Armadura comprada!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")

    def comprar_hearthstone(self):
        if self.ventana.campeon.puntos >= self.objetos_disponibles["Carta Hearthstone"].precio:
            self.ventana.campeon.puntos -= self.objetos_disponibles["Carta Hearthstone"].precio
            a = random.choice(["velocidad", "dano", "resistencia", "vida", "distancia"])
            if a == "velocidad":
                self.ventana.campeon.velocidad += self.objetos_disponibles["Carta Hearthstone"].atributo[1]
            elif a == "dano":
                self.ventana.campeon.dano += self.objetos_disponibles["Carta Hearthstone"].atributo[1]
            elif a == "resistencia":
                self.ventana.campeon.resistencia += self.objetos_disponibles["Carta Hearthstone"].atributo[1]
            elif a == "vida":
                self.ventana.campeon.health += self.objetos_disponibles["Carta Hearthstone"].atributo[1]
            else:
                self.ventana.campeon.distancia += self.objetos_disponibles["Carta Hearthstone"].atributo[1]
            self.objetos_disponibles["Carta Hearthstone"].atributo[1] = round(
                self.objetos_disponibles["Carta Hearthstone"].atributo[1] * 1.5)
            self.objetos_disponibles["Carta Hearthstone"].precio += self.objetos_disponibles["Carta Hearthstone"].precio / 2
            print("Carta hearthstone comprada!")
        else:
            QMessageBox.warning(self.ventana, "", "Puntos insuficientes!")


class Objeto:
    def __init__(self, name, precio_inicial, atributo):
        self.nombre = name
        self.precio = precio_inicial
        self.atributo = atributo



