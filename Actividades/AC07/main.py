__author__ = 'Ignacio Castaneda, Diego Iruretagoyena, Ivania Donoso, CPB'

import random
from datetime import datetime as dt


"""
Escriba sus decoradores y funciones auxiliares en este espacio.
"""

def log(f):
    def decorador(*args, **kwargs):
        file = open("log.txt", "a")
        line = ""
        if f.__name__ == "crear_cuenta":
            line = str(dt.now())+":"+ "-" + "Creacion de Cuenta :"
        elif f.__name__ == "transferir":
            line = str(dt.now()) + ":" + "-" + "Transaccion :"
        elif f.__name__ == "invertir":
            line = str(dt.now()) + ":" + "-" + "Inversion :"
        elif f.__name__ == "crear_cuenta":
            line = str(dt.now()) + ":" + "-" + "Creacion de Cuenta :"
        elif f.__name__ == "saldo":
            line = str(dt.now()) + ":" + "-" + "Saldo :"
        for arg in args:
            line += ", " + str(arg)

        for k,v in kwargs.items():
            line += ", "+str(k)+"-"+str(v)
        line += "\n"
        file.write(line)
        file.close()
        return f(*args)
    return decorador


def verificar_transferencia(f):
    def decorador(self, origen, destino, monto, clave):
        if origen not in self.cuentas:
            raise AssertionError("Cuenta de origen no existe")
        elif destino not in self.cuentas:
            raise AssertionError("Cuenta de Destino no existe")
        elif self.cuentas[origen].saldo < monto:
            raise AssertionError ("Saldo insuficiente")
        elif clave != self.cuentas[origen].clave:
            raise AssertionError ("Clave incorrecta!")
        else:
            return f(self,origen,destino,monto,clave)

    return decorador


def verificar_inversion(f):
    def decorador(self, cuenta, monto, clave):
        if cuenta not in self.cuentas:
            raise AssertionError("Cuenta de origen no existe")
        elif self.cuentas[cuenta].saldo < monto:
            raise AssertionError("Saldo insuficiente...")
        elif self.cuentas[cuenta].clave != clave:
            raise AssertionError("Clave incorrecta")
        elif self.cuentas[cuenta].inversiones + monto > 10000000:
            raise AssertionError("Monto de total de inversiones superior a 10.000.000")
        else:
            return f(self, cuenta, monto, clave)

    return decorador


def verificar_cuenta(f):
    def decorador(self, nombre, rut, clave, numero, saldo_inicial=0):
        if numero in self.cuentas:
            numero_nuevo = self.crear_numero()
            decorador(self, nombre, rut, clave, numero_nuevo, saldo_inicial)
        elif len(clave) != 4:
            raise AssertionError("Clave de tamano distinto a 4")
        elif len(str(rut).split("-")) > 2:
            raise AssertionError("Rut contiene mas de un guion")
        lista = str(rut).split("-")
        for p in lista:
            try:
                h = int(p)
            except Exception:
                raise AssertionError("Caracteres invalidos")
        return f(self, nombre, rut, clave, numero, saldo_inicial)
    return decorador


def verificar_saldo(f):
    def decorador(self, numero_cuenta):
        if numero_cuenta not in self.cuentas:
            raise AssertionError("Cuenta no existe")
        elif f(self,numero_cuenta)!= self.cuentas[numero_cuenta].saldo:
            return f(self,numero_cuenta)/5
    return decorador



"""
No pueden modificar nada más abajo, excepto para agregar los decoradores a las 
funciones/clases.
"""

class Banco:
    def __init__(self, nombre, cuentas=None):
        self.nombre = nombre
        self.cuentas = cuentas if cuentas is not None else dict()
    @log
    @verificar_saldo
    def saldo(self, numero_cuenta):
        # Da un saldo incorrecto
        return self.cuentas[numero_cuenta].saldo * 5
    @log
    @verificar_transferencia
    def transferir(self, origen, destino, monto, clave):
        # No verifica que la clave sea correcta, no verifica que las cuentas 
        # existan
        self.cuentas[origen].saldo -= monto
        self.cuentas[destino].saldo += monto
    @log
    @verificar_cuenta
    def crear_cuenta(self, nombre, rut, clave, numero, saldo_inicial=0):
        # No verifica que el número de cuenta no exista
        cuenta = Cuenta(nombre, rut, clave, numero, saldo_inicial)
        self.cuentas[numero] = cuenta
    @log
    @verificar_inversion
    def invertir(self, cuenta, monto, clave):
        # No verifica que la clave sea correcta ni que el monto de las 
        # inversiones sea el máximo
        self.cuentas[cuenta].saldo -= monto
        self.cuentas[cuenta].inversiones += monto

    def __str__(self):
        return self.nombre

    def __repr__(self):
        datos = ''

        for cta in self.cuentas.values():
            datos += '{}\n'.format(str(cta))

        return datos

    @staticmethod
    def crear_numero():
        return int(random.random() * 100)


class Cuenta:
    def __init__(self, nombre, rut, clave, numero, saldo_inicial=0):
        self.numero = numero
        self.nombre = nombre
        self.rut = rut
        self.clave = clave
        self.saldo = saldo_inicial
        self.inversiones = 0

    def __repr__(self):
        return "{} / {} / {} / {}".format(self.numero, self.nombre, self.saldo,
                                          self.inversiones)


if __name__ == '__main__':
    bco = Banco("Santander")
    bco.crear_cuenta("Mavrakis", "4057496-7", "1234", bco.crear_numero())
    bco.crear_cuenta("Ignacio", "19401259-4", "1234", 1, 24500)
    bco.crear_cuenta("Diego", "19234023-3", "1234", 2, 13000)
    try:
        bco.crear_cuenta("Juan", "19231233--3", "1234", bco.crear_numero())
    except AssertionError as msg:
        print('Error', msg)

    print(repr(bco))


    """
    Estos son solo algunos casos de pruebas sugeridos. Sientase libre de agregar 
    las pruebas que estime necesaria para comprobar el funcionamiento de su 
    solucion.
    """

    try:
        print(bco.saldo(10))
    except AssertionError as error:
        print('Error: ', error)

    try:
        print(bco.saldo(1))
    except AssertionError as error:
        print('Error: ', error)

    try:
        bco.transferir(1, 2, 5000, "1234")
    except AssertionError as msg:
        print('Error: ', msg)


    try:
        bco.transferir(1, 2, 5000, "4321")
    except AssertionError as msg:
        print('Error: ', msg)

    print(repr(bco))
    print()

    try:
        bco.invertir(2, 200000, "1234")
    except AssertionError as error:
        print('Error: ', error)
    print(repr(bco))

    try:
        bco.invertir(2, 200000, "4321")
    except AssertionError as error:
        print('Error: ', error)
    print(repr(bco))
