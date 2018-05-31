#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lector import *
from SuperLuchin import *


class Clima:
    def __init__(self, id):
        self.lista = abrir("meteorologia.csv")
        self.id = str(id)
        for k in self.lista:
            if k[0] == self.id:
                fecha_inicio = k[1]
                fecha_inicio = fecha_inicio.split(" ")
                self.fecha_inicio = Hora_Fecha(fecha_inicio[0], fecha_inicio[1])
                fecha_termino = k[2]
                fecha_termino = fecha_termino.split(" ")
                self.fecha_termino = Hora_Fecha(fecha_termino[0], fecha_termino[1])
                self.tipo = k[3]
                self.valor = k[4]
                self.lat = float(k[5])
                self.lon = float(k[6])
                self.radio = float(k[6])
                self.lon_max = self.lon + (1/110000)*self.radio
                self.lon_min = self.lon - (1/110000)*self.radio
                self.lat_max = self.lat + (1/110000)*self.radio
                self.lat_min = self.lat - (1/110000)*self.radio

    def check_clima(self, hora_actual):
        clima_activo = []
        for f in self.lista:
            if "id:string" == f[0]:
                continue
            hora_clima1 = f[1].split(" ")
            clima1 = Hora_Fecha(hora_clima1[0], hora_clima1[1])
            hora_clima2 = f[2].split(" ")
            clima2 = Hora_Fecha(hora_clima2[0], hora_clima2[1])
            if hora_actual >= clima1.hora and clima2.hora >= hora_actual:
                clima = Clima(f[0])
                clima_activo.append(clima)

        return clima_activo