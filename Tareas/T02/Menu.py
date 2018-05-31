from cargar import cargar_juego
from Plague import *
from connections_generator import *


class Menu:
    def __init__(self):
        print(" ")
        print("----- Bienvenido a Pandemic! -----")
        while True:
            print("")
            print("1) Iniciar Juego Nuevo")
            print("2) Cargar Juego Anterior")
            print(" ")
            desicion = str(input("Ingresa opción: "))
            if desicion == "1":
                generate_connections()
                self.juego_nuevo()
            elif desicion == "2":
                self.cargar_juego()
            else:
                print("")
                print("Error en la seleccion intenta nuevamente")
            break

    def juego_nuevo(self):
        print("")
        name = str(input("Ingrese nombre de la infeccion (nota: con este nombre podras cargar luego este juego) "))
        print("")
        print(" Elige el tipo de infeccion!")
        print("")
        print("1) Virus")
        print("2) Bacteria")
        print("3) Parasito")
        print("")
        eleccion = str(input("Eleccion: "))
        if eleccion == "1":
            pais_inicial = str(input("Ingresa el primer pais infectado: "))
            juego = Pandemic("Virus", name, pais_inicial)
            juego.start()
        elif eleccion == "2":
            pais_inicial = str(input("Ingresa el primer pais infectado: "))
            juego = Pandemic("Bacteria", name, pais_inicial)
            juego.start()
        elif eleccion == "3":
            pais_inicial = str(input("Ingresa el primer pais infectado: "))
            juego = Pandemic("Parasito", name, pais_inicial)
            juego.start()
        else:
            print("Hubo un error en la seleccion, intenta nuevamente")
            self.juego_nuevo()

    def cargar_juego(self):
        try:
            print("")
            nombre = str(input("Ingresa el nombre de la infeccion: "))
            juego = cargar_juego(nombre)
            juego.start()
        except AttributeError:
            print("")
            print("Intentalo Nuevamente!")
            self.cargar_juego()

