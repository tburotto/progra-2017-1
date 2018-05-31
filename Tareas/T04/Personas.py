from abc import ABCMeta, abstractmethod
import random
import time

# Este modulo pretende
# implementar las clases, alumnos, ayudantes
# profesores y coordinador

# Funciones necesarias

def Dificultad(materia):
    dic = {"oop":2,"herencia":2,"edd":3,"arbol":5,"funcional":7,
           "meta":10,"simulacion":7,"thred":9,
           "interfaz":1,"bytes":6,"network":6,"webservices":5}

    for k,v in dic:
        if k == materia:
            return v
        else:
            continue

    raise AssertionError("Materia no hayada!")

# Clases


class Alumno(metaclass=ABCMeta):
    def __init__(self, name):
        self.visita_anterior = [0, False]
        self.name = name
        self.confianza = random.uniform(2, 12)
        self.confianza_inicial = self.confianza
        self.manejo_contenidos = 0
        self.creditos = 0
        self.seccion = None
        self.horas_semana = 0
        self.notas_esperadas = {"Tareas": [], "Controles": [], "Actividades": [], "Examen": []}
        self.notas_obtenidas = {"Tareas": [], "Controles": [], "Actividades": [], "Examen": []}
        self.aumento_semanal = 0

        while self.creditos == 0:
            ocurrencia = random.random()
            if ocurrencia <= 0.05:
                self.creditos = 60
            elif ocurrencia <= 0.1:
                self.creditos = 40
            elif ocurrencia <= 0.15:
                self.creditos = 55
            elif ocurrencia <= 0.7:
                self.creditos = 50

        self.nivel_programacion = random.uniform(2,10)
        self.nivel_programacion2 = self.nivel_programacion
        self.progreso = 0
        self.horas_dedicadas_a_contenidos = 0
        self.horas_dedicadas_a_tareas = 0
        # De Aqui para abajo estan los manejos de contenidos
        self.oop = 0
        self.herencia = 0
        self.edd = 0
        self.arbol = 0
        self.funcional = 0
        self.meta = 0
        self.simulacion = 0
        self.thred = 0
        self.interfaz = 0
        self.bytes = 0
        self.network = 0
        self.webservices = 0

    @property
    def promedio(self):
        suma = 0
        for control in self.notas_obtenidas["Controles"]:
            suma += control
        try:
            pcontrol = suma/len(self.notas_obtenidas["Controles"])
        except ZeroDivisionError:
            pcontrol = 1
        suma = 0
        for tarea in self.notas_obtenidas["Tareas"]:
            suma += tarea
        try:
            ptareas = suma/len(self.notas_obtenidas["Tareas"])
        except ZeroDivisionError:
            ptareas = 1
        suma = 0
        for actividades in self.notas_obtenidas["Actividades"]:
            suma += actividades
        try:
            pactividades = suma/len(self.notas_obtenidas["Actividades"])
        except ZeroDivisionError:
            pactividades = 1
        suma = 0
        for pregunta in self.notas_obtenidas["Examen"]:
            suma += pregunta
        try:
            pexamen = suma/len(self.notas_obtenidas["Examen"])
        except ZeroDivisionError:
            pexamen = 1
        promedio = 0.25*pactividades + 0.4*ptareas + 0.2*pcontrol + 0.15*pexamen
        return promedio

    @property
    def manejo(self):
        suma = self.oop + self.herencia + self.edd + self.arbol + \
               self.funcional + self.meta + self.simulacion + self.thred + self.interfaz + \
               self.bytes + self.network + self.webservices
        promedio = suma/12
        return promedio

    def nivel_original(self):
        self.nivel_programacion = self.nivel_programacion2

    def calcular_manejo(self, materia):
        if materia == "oop":
            self.oop = 1 / 2 * self.horas_dedicadas_a_contenidos
        elif materia == "herencia":
            self.herencia = 1 / 2 * self.horas_dedicadas_a_contenidos
        elif materia == "edd":
            self.edd = 1 / 3 * self.horas_dedicadas_a_contenidos
        elif materia == "arbol":
            self.arbol = 1 / 5 * self.horas_dedicadas_a_contenidos
        elif materia == "funcional":
            self.funcional = 1 / 7 * self.horas_dedicadas_a_contenidos
        elif materia == "meta":
            self.meta = 1 / 10 * self.horas_dedicadas_a_contenidos
        elif materia == "simulacion":
            self.simulacion = 1 / 7 * self.horas_dedicadas_a_contenidos
        elif materia == "thred":
            self.thred = 1 / 9 * self.horas_dedicadas_a_contenidos
        elif materia == "interfaz":
            self.interfaz = 1 * self.horas_dedicadas_a_contenidos
        elif materia == "bytes":
            self.bytes = 1 / 6 * self.horas_dedicadas_a_contenidos
        elif materia == "network":
            self.network = 1 / 6 * self.horas_dedicadas_a_contenidos
        elif materia == "webservices":
            self.webservices = 1 / 5 * self.horas_dedicadas_a_contenidos

    def actualizar_horas_dedicadas(self):
        horas = round(self.horas_semana*0.3)
        horas2 = round(self.horas_semana*0.7)
        self.horas_dedicadas_a_contenidos = horas
        self.horas_dedicadas_a_tareas = horas2

    def calcular_horas_semanas(self):
        if self.creditos == 40:
            horas = random.uniform(10, 25)
        elif self.creditos == 50:
            horas = random.uniform(10, 15)
        elif self.creditos == 55:
            horas = random.uniform(5, 15)
        else:
            horas = random.uniform(5, 10)
        self.horas_semana = horas

    def materia(self,materia):
        if materia == "oop":
            return self.oop
        elif materia == "herencia":
            return self.herencia
        elif materia == "edd":
            return self.edd
        elif materia == "arbol":
            return self.arbol
        elif materia == "funcional":
            return self.funcional
        elif materia == "meta":
            return self.meta
        elif materia == "simulacion":
            return self.simulacion
        elif materia == "thred":
            return self.thred
        elif materia == "interfaz":
            return self.interfaz
        elif materia == "bytes":
            return self.bytes
        elif materia == "network":
            return self.network
        elif materia == "webservices":
            return self.webservices

    def actualizar_nivel_programacion(self):
        self.nivel_programacion += self.nivel_programacion*0.05

    def calcular_confianza(self, control, tarea):
        x = 1
        y = 0
        z = 0
        nota_esperada_control = 0
        nota_obtenida_control = 0
        nota_esperada_tarea = 0
        nota_obtenida_tarea = 0
        if control == True:
            y = 1
            nota_esperada_control = self.notas_esperadas["Controles"][-1]
            nota_obtenida_control = self.notas_obtenidas["Controles"][-1]
        if tarea == True:
            nota_esperada_tarea = self.notas_esperadas["Tareas"][-1]
            nota_obtenida_tarea = self.notas_obtenidas["Tareas"][-1]
            z = 1

        nota_esperada_actividad = self.notas_esperadas["Actividades"][-1]
        nota_obtenida_actividad = self.notas_obtenidas["Actividades"][-1]
        confianza_notas = 3*x*(nota_obtenida_actividad - nota_esperada_actividad)+ z*(nota_obtenida_control-nota_esperada_control) + 5*y*(nota_esperada_tarea-nota_obtenida_tarea)
        self.confianza += confianza_notas
        if self.confianza <= 0:
            self.confianza = 0






class AlumnoTeorico(Alumno):
    def __init__(self, name):
        super().__init__(name)


class AlumnoEficiente(Alumno):
    def __init__(self, name):
        super().__init__(name)
        pass


class AlumnoArtistico(Alumno):
    def __init__(self, name):
        super().__init__(name)


class Ayudante(metaclass=ABCMeta):
    def __init__(self, nombre):
        self.nombre = nombre


class Ayudante_Tareas(Ayudante):
    def __init__(self, nombre):
        super().__init__(nombre)



class Ayudante_Docencia(Ayudante):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def materias(self):
        contenidos = ["oop","herencia","edd","arbol","funcional", "meta",
                      "simulacion", "thred", "interfaz", "bytes", "network", "webservices"]

        r1 = random.choice(contenidos)
        contenidos.remove(r1)
        r2 = random.choice(contenidos)
        contenidos.remove(r2)
        r3 = random.choice(contenidos)
        contenidos.remove(r3)
        return [r1, r2, r3]


class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seccion = None


class Coordinador:
    def __init__(self, nombre="DR.MAVRAKIS"):
        self.nombre = nombre


if __name__ == "__main__":
    A1 = AlumnoArtistico("1")



