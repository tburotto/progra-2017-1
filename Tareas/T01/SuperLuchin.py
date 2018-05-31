#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lector
from abc import abstractmethod, ABCMeta
from math import pi


class Usuario(metaclass=ABCMeta):
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
        self.hora = 0
        self.identidad = "N\A"
        lista = lector.abrir("usuarios.csv")
        for k in lista:
            if self.usuario in k and self.clave in k:
                self.identidad = k[3]
                self.tupla = k
        if len(self.identidad) < 2:
            self.identidad = "ANAF"

    @abstractmethod
    def ingresar(self):
        pass

    @abstractmethod
    def ConsultasBasicas(self, desicion):
        pass

    @abstractmethod
    def ConsultasAvanzadas(self):
        pass


class Usuario_Anaf(Usuario):
    def __init__(self, usuario, clave):
        super().__init__(usuario, clave)

    def ingresar(self):
        lista = lector.abrir("usuarios.csv")
        for k in lista:
            if self.usuario in k:
                if k[2] == self.clave:
                    if self.identidad == "ANAF":
                        print("Bienvenido " + k[1])
                        return True
                    else:
                        print("No es ANAF")
                        return False
                else:
                    print("Clave incorrecta!")
                    return False
        return False

    def ConsultasBasicas(self, desicion):
        if desicion == 1:
            print("")
            print("1) Leer Usuarios")
            print("2) Leer Incendios")
            print("3) Leer Recursos")
            desicion4 = str(input("Eleccion: "))
            if desicion4 == "1":
                self.leer_usuarios()
            elif desicion4 == "2":
                self.leer_incendios()
        elif desicion == 2:
            nombre_usuario = str(input("Ingresar nombre usuario: "))
            clave = str(input("Ingresar contraseña usuario: "))
            recurso = str(input("Ingresar recurso: (si es ANAF presionar enter)"))
            lista = lector.abrir("usuarios.csv")
            last_id = int(lista[-1][0])
            n_id = str(last_id + 1)
            line = n_id + "," + nombre_usuario + "," + clave + "," + recurso
            lector.crearlinea(line, "usuarios.csv")
        elif desicion == 3:
            lat = str(input("Ingresar latitud: "))
            lon = str(input("Ingresar longitud: "))
            pot = str(input("Ingresar potencia: "))
            fecha = str(input("Ingresar fecha y hora: "))
            lista = lector.abrir("incendios.csv")
            last_id = int(lista[-1][0])
            n_id = str(last_id + 1)
            line = n_id + "," + lat + "," + lon + "," + pot + "," + fecha
            lector.crearlinea(line, "incendios.csv")
        elif desicion == 4:
            f_incio = str(input("Ingresar fecha y hora inicio: "))
            f_termino = str(input("Ingresar fecha y hora termino: "))
            tipo = str(input("Ingresar tipo: "))
            lat = str(input("Ingresar latitud: "))
            lon = str(input("Ingresar longitud: "))
            radio = str(input("Ingresar radio: "))
            lista = lector.abrir("meteorologia.csv")
            last_id = int(lista[-1][0])
            n_id = str(last_id + 1)
            line = n_id + "," + f_incio + "," + f_termino + "," + tipo + "," + lat + "," + lon + "," + radio
            lector.crearlinea(line, "meteorologia.csv")

    def ConsultasAvanzadas(self):
        print("")
        while True:
            print("Elige una Opcion: ")
            print("1) Incendios Activos")
            print("2) Incendios Apagados")
            print("3) Recursos mas utilizados")
            print("4) Recursos mas efectivos")
            print("5) Volver")
            desicion2 = str(input("Opcion: "))
            if desicion2 == "1":
                incendios_activos = self.Incendios_Activos()
                print(incendios_activos)
                for k in incendios_activos:
                    print(k)
                break
            elif desicion2 == "2":
                pass
            elif desicion2 == "3":
                pass
            elif desicion2 == "4":
                pass
            elif desicion2 == "5":
                break

    def Incendios_Activos(self):
        incendios_activos = []
        lista = lector.abrir("incendios.csv")
        for k in lista:
            if k[0] == "id:string":
                continue
            incendio = Incendio(k[0], self.hora)
            if self.hora >= incendio.fecha:
                incendios_activos.append(incendio)
        i = 0
        for k in incendios_activos:
            if k.puntos_poder <= 0:
                incendios_activos.pop(i)
            i += 1
        return incendios_activos

    def leer_incendios(self):
        print("")
        nid = str(input("Ingresa el numero de id del incendio que deseas consultar:"))
        incendios = lector.abrir("incendios.csv")
        incendio = 0
        for k in incendios:
            if nid == k[0]:
                incendio = k
        if incendio != 0:
            print("ID:" + incendio[0] + ", lat: " + incendio[1] + ", lon: " + incendio[2] + ", potencia: " + incendio[
                3] + ", fecha inicio: " + incendio[4])
        else:
            print("No se encontro el id")

    def leer_usuarios(self):
        print("")
        nid = str(input("Ingresa el numero de id del usuario que deseas consultar: "))
        usuarios = lector.abrir("usuarios.csv")
        usuario = 0
        for k in usuarios:
            if nid == k[0]:
                usuario = k
        if usuario != 0:
            print("ID:" + usuario[0] + ", nombre: " + usuario[1] + ", contraseña: " + usuario[2] + ", recurso: " + usuario[
                3])


class Usuario_Jefes_Piloto(Usuario):
    def __init__(self, usuario, clave):
        super().__init__(usuario, clave)

    def ingresar(self):
        lista = lector.abrir("usuarios.csv")
        for k in lista:
            if self.usuario in k:
                if k[2] == self.clave:
                    if self.identidad != "ANAF":
                        print("Bienvenido " + k[1])
                        return True
                    else:
                        print("No es Jefe o Piloto")
                        return False
                else:
                    print("Clave incorrecta!")
                    return False
        return False

    def ConsultasBasicas(self, desicion):
        if desicion == 1:
                print("")
                nid = str(input("Ingresa el numero de id del incendio que deseas consultar:"))
                incendios = lector.abrir("incendios.csv")
                incendio = 0
                for k in incendios:
                    if nid == k[0]:
                        incendio = k
                if incendio != 0:
                    print("ID:" + incendio[0] + ", lat: " + incendio[1] + ", lon: " + incendio[2] + ", potencia: " +
                          incendio[
                              3] + ", fecha inicio: " + incendio[4])
                else:
                    print("No se encontro el id")

        if desicion == 2:
            print("")
            nid = str(input("Ingresa el numero de id del recurso que deseas consultar:"))
            recursos = lector.abrir("recursos.csv")
            recurso = 0
            for k in recursos:
                if nid == k[0]:
                    recurso = k
            if recurso != 0:
                print("ID:" + recurso[0] + ", tipo: " + recurso[1] + ", lat base recurso: " +
                      recurso[2] + ", lon base recurso: " +
                      recurso[
                          3] + ", velocidad: " + recurso[4] + ", autonomia: " + recurso[5] + ", delay: "+ recurso[6] +
                      ", tasa extincion: " + recurso[7] + ", costo: " + recurso[8])
            else:
                print("No se encontro el id")

    def ConsultasAvanzadas(self):
        pass


class Hora_Fecha:

    def __init__(self, fecha, hora):
        self.hora = hora
        self.fecha = fecha
        self.lista_hora = self.hora.split(":")
        self.lista_fecha = self.fecha.split("-")

    def __ge__(self, other):
        if int(self.lista_fecha[0]) > int(other.lista_fecha[0]):
            return True
        elif int(self.lista_fecha[1]) > int(other.lista_fecha[1]) and int(self.lista_fecha[0]) == int(other.lista_fecha[0]):
            return True
        elif int(self.lista_fecha[2]) > int(other.lista_fecha[2]) \
                and int(self.lista_fecha[1]) == int(other.lista_fecha[1]) and \
                        int(self.lista_fecha[0]) == int(other.lista_fecha[0]):
            return True
        if self.fecha == other.fecha:
            if int(self.lista_hora[0]) > int(other.lista_hora[0]):
                return True
            elif int(self.lista_hora[1]) > int(other.lista_hora[1]) and int(self.lista_hora[0]) == int(
                    other.lista_hora[0]):
                return True
            elif int(self.lista_hora[2]) >= int(other.lista_hora[2]) and int(self.lista_hora[1]) == int(
                    other.lista_hora[1]) and int(self.lista_hora[0]) == int(other.lista_hora[0]):
                return True
        return False

    def __sub__(self, other):
        cuenta = 0
        if self.lista_fecha[1] != other.lista_fecha[1]:
            cuenta += int(other.lista_hora[0])
            print(cuenta)
            dias = 30 - int(other.lista_fecha[2])
            cuenta += dias*24
            print(cuenta)
            meses = (int(self.lista_fecha[1]) - int(other.lista_fecha[1])) - 1
            if meses == - 1:
                meses = 0
            cuenta += meses*30*24
            print(cuenta)
            cuenta += int(self.lista_fecha[2])*24 + int(self.lista_hora[0])

        elif self.lista_fecha[2] != other.lista_fecha[2]:
            cuenta += 24 - int(other.lista_hora[0])
            dias = int(self.lista_fecha[2]) - int(other.lista_fecha[2]) - 1
            if dias == - 1:
                dias = 0
            cuenta += dias*24
            cuenta += int(self.lista_hora[0])
        else:
            cuenta += int(self.lista_hora[0]) - int(other.lista_hora[0])
        return cuenta

    def __str__(self):
        return str(str(self.fecha)+" "+str(self.hora))


class Incendio:
    def __init__(self, id, hora_actual):
        self.hora_actual = hora_actual
        self.id = str(id)
        incendios = lector.abrir("incendios.csv")
        self.radio = 0
        self.lat = 0
        self.lon = 0
        self.potencia = 0
        for k in incendios:
            if k[0] == "id:string":
                continue
            if self.id == k[0]:
                self.lat = float(k[1])
                self.lon = float(k[2])
                self.potencia = int(k[3])
                fecha = k[4].split(" ")
                self.fecha = Hora_Fecha(fecha[0], fecha[1])
        self.check_radio()
        self.area = pi * (self.radio**2)
        self.puntos_poder = self.area * self.potencia
        self.lon_max = self.lon + (1/110000)*self.radio
        self.lon_min = self.lon - (1/110000)*self.radio
        self.lat_max = self.lat + (1/110000)*self.radio
        self.lat_min = self.lat - (1/110000)*self.radio

    def check_radio(self):
        horas = self.hora_actual - self.fecha
        self.radio = 500*horas

    def check_viento(self, clima, horas):
        self.radio += float(clima.valor)*(10**(-2))*horas

    def check_lluvia(self, clima, horas):
        self.radio -= float(clima.valor)*50*horas

    def check_temperatura(self, clima, horas):
        if int(float(clima.valor)) > 30:
            valor = int(float(clima.valor)) - 30
            self.radio += valor*25*horas

    def __str__(self):
        return str("ID:" + str(self.id) + ", lat: " + str(self.lat) +
                   ", lon: " + str(self.lon) + ", potencia: " + str(self.potencia) +
                   ", fecha inicio: "+str(self.fecha))


class Estrategias:
    def __init__(self):
        pass

    def costo(self):
        pass

    def tiempo(self):
        pass

    def cantidad(self):
        pass

