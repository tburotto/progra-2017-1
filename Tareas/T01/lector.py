#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Este es el modulo que leera los archivos csv

__author__ = "Tomas Burotto"


def abrir(nombre):
    lista_nueva = []
    with open(nombre) as f:
        lista = f.readlines()
        for k in lista:
             j = k.split(",")
             lista_nueva.append(j)
    lista_nueva.pop(0)
    return lista_nueva


def crearlinea(linea, nombre):
    file = open(nombre, "a")
    file.write(linea+"\n")
    file.close()




