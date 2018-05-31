import unittest
from main import *

class TestearFormato(unittest.TestCase):

    def setUp(self):
        self.archivo = open("mensaje_marciano.txt", "r")
        self.lineas = self.archivo.readlines()
        self.texto = "".join(self.lineas).replace('\n', '')
        self.codigo = self.texto.split(" ")

    def test_archivo(self):
        cantidad = 0
        suma = 0
        for i in self.codigo:
            for k in i:
                cantidad += 1
                suma += int(k)
        self.assertEquals(cantidad, 408)
        self.assertEquals(suma, 253)

    def tearDown(self):
        self.archivo.close()


class TestearMensaje(unittest.TestCase):
    def setUp(self):
        self.descifrador = Descifrador("mensaje_marciano.txt")
        self.archivo = open("mensaje_marciano.txt", "r")
        self.lineas = self.archivo.readlines()
        self.texto = "".join(self.lineas).replace('\n', '')
        self.codigo = self.texto.split(" ")

    def test_incorrectos(self):
        pass

    def test_caracteres(self):
        pass

    def test_codificacion(self):
        for i in self.codigo:
            for k in i:
                self.assertEquals(k, "1" or "0")

    def tearDown(self):
        self.archivo.close()

