#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lector
from Inicializacion import *
import SuperLuchin
from abc import ABCMeta,abstractmethod


class Menu:
    def __init__(self):
        self.usuario = 0
        self.clave = ""
        self.username = ""
        self.hora = 0

    def start(self):
        print("BIENVENIDO A SUPER LUCHIN")
        self.username = str(input("Ingrese Usuario: "))
        self.clave = str(input("Ingrese Contraseña: "))

        if SuperLuchin.Usuario_Anaf(self.username, self.clave).ingresar():
            self.usuario = SuperLuchin.Usuario_Anaf(self.username, self.clave)
            self.hora = str(input("Ingrese la fecha y hora actual: "))
            self.hora = self.hora.split(" ")
            self.usuario.hora = SuperLuchin.Hora_Fecha(self.hora[0], self.hora[1])
            Menu_Anaf(self.usuario).Opciones()
            Inicializar_Clima(self.hora[0], self.hora[1])

        elif SuperLuchin.Usuario_Jefes_Piloto(self.username, self.clave).ingresar():
            self.usuario = SuperLuchin.Usuario_Jefes_Piloto(self.username, self.clave)
            self.hora = str(input("Ingrese la fecha y hora actual: "))
            self.hora = self.hora.split(" ")
            self.usuario.hora = SuperLuchin.Hora_Fecha(self.hora[0], self.hora[1])
            Menu_Jefes_Pilotos(self.usuario).Opciones()
            Inicializar_Clima(self.hora[0], self.hora[1])

        else:
            menu.start()


class Menu_Anaf(Menu):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def Opciones(self):
        while True:
            print("")
            print("Estas son tus opciones: ")
            print("1) Consultas basicas")
            print("2) Consultas avanzadas")
            print("3) Estrategias de extincion")
            print("4) Cambiar de usuario")
            print("5) Salir")
            print("")
            decision = str(input("¿Que deseas hacer? "))
            if decision == "1":
                print("")
                print("Estas son tus opciones: ")
                print("1) Buscar de base de datos ")
                print("2) Crear Usuario")
                print("3) Agregar Incendio")
                print("4) Agregar Pronostico")
                decision3 = str(input("¿Que deseas hacer?"))
                if decision3 == "1":
                    self.usuario.ConsultasBasicas(1)
                elif decision3 == "2":
                    self.usuario.ConsultasBasicas(2)
                elif decision3 == "3":
                    self.usuario.ConsultasBasicas(3)
                elif decision3 == "4":
                    self.usuario.ConsultasBasicas(4)

            elif decision == "2":
                self.usuario.ConsultasAvanzadas()
            elif decision == "3":
                continue
            elif decision == "4":
                Menu_Anaf(self.usuario).CambiarUsuario()
                break
            elif decision == "5":
                break
            else:
                print("Hubo un error en la selección")

    def CambiarUsuario(self):
        Menu().start()


class Menu_Jefes_Pilotos(Menu):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def Opciones(self):
        while True:
            print("")
            print("Estas son tus opciones: ")
            print("1) Consultas basicas")
            print("2) Cambiar de usuario")
            print("3) Salir")
            print("")
            decision = str(input("¿Que deseas hacer? "))
            if decision == "1":
                print("")
                print("Estas son tus opciones: ")
                print("1) Leer Incendios asignados ")
                print("2) Leer recursos asignados")
                print("")
                decision3 = str(input("¿Que deseas hacer?"))
                if decision3 == "1":
                    self.usuario.ConsultasBasicas(1)
                elif decision3 == "2":
                    self.usuario.ConsultasBasicas(2)

            elif decision == "2":
                Menu_Jefes_Pilotos(self.usuario).CambiarUsuario()
                break
            elif decision == "3":
                break
            else:
                print("Hubo un error en la selección")

    def CambiarUsuario(self):
        Menu().start()

# usuario = SuperLuchin.Usuario("Amadeo", "f9Ad8C7%Es")
