from Funciones import Dificultad, nota_esperada
from Estadisticas import grafico, estadisticas_finales, estadisticas_personales
import csv
from collections import deque
import random
from Personas import AlumnoTeorico, AlumnoArtistico, AlumnoEficiente, \
    Ayudante_Docencia, Ayudante_Tareas, Profesor, Coordinador


class Simulacion:
    def __init__(self, prob40=0.4, prob50=0.7,prob55=0.15, prob60=0.05, probprof=0.2, probatraso=0.15, probmail=0.2,
                 probfiesta=1/30, probfutbol=1/70, confianzainf=2, confianzasup=12):
        self.prob40 = (prob40)
        self.prob50 = (prob50)
        self.prob55 = (prob55)
        self.prob60 = (prob60)
        self.probprof = (probprof)
        self.probatraso = (probatraso)
        self.probmail = (probmail)
        self.probfiesta = (probfiesta)
        self.probfutbol = (probfutbol)
        self.confianzasup = (confianzasup)
        self.confianzainf = (confianzainf)
        if self.prob40 == "-":
            self.prob40 = 0.4
        if self.prob50 == "-":
            self.prob50 = 0.7
        if self.prob50 == "-":
            self.prob50 = 0.7
        if self.prob55 == "-":
            self.prob55 = 0.15
        if self.prob60 == "-":
            self.prob60 = 0.05
        if self.probprof == "-":
            self.probprof = 0.7
        if self.probatraso == "-":
            self.probatraso = 0.15
        if self.probmail == "-":
            self.probmail = 0.2
        if self.probfiesta == "-":
            self.probfiesta = 1/30
        if self.probfutbol == "-":
            self.probfutbol = 1/70
        if self.confianzasup == "-\n":
            self.confianzasup = 12
        if self.confianzainf == "-\n":
            self.confianzainf = 2
        self.prob40 = float(self.prob40)
        self.prob50 = float(self.prob50)
        self.prob55 = float(self.prob55)
        self.prob60 = float(self.prob60)
        self.probprof = float(self.probprof)
        self.probatraso = float(self.probatraso)
        self.probmail = float(self.probmail)
        self.probfiesta = float(self.probfiesta)
        self.probfutbol = float(self.probfutbol)
        self.confianzasup = float(self.confianzasup)
        self.confianzainf = float(self.confianzainf)

        self.actividades_grafico = []
        self.tareas_grafico = []
        self.semana = 0
        self.controles_grafico = []
        self.tarea_semana = False
        self.control_semana = False
        self.tareas = 0
        self.materias_tarea = []
        self.exigencia_tarea = 0
        self.notas = {"Tareas": [], "Controles": [], "Actividades": [], "Examen": []}
        self.controles = 0
        self.control_semana_pasada = False
        self.dia = 1
        self.secciones = None
        self.next_tarea = 5
        self.alumnos = []
        self.ayudantes_docencia = []
        self.ayudantes_tareas = []
        self.profesores = []
        self.coordinador = None
        self.materias2 = ["oop", "herencia", "edd", "arbol", "funcional", "meta",
                      "simulacion", "thred", "interfaz", "bytes", "network", "webservices"]
        self.materias = deque(["oop","herencia","edd","arbol","funcional", "meta",
                      "simulacion", "thred", "interfaz", "bytes", "network", "webservices"])
        self.exigencia_actividad = None
    @property
    def aprobados(self):
        i = 0
        for alumno in self.alumnos:
            if alumno.promedio >= 4:
                i += 1
        return i/self.n_alumnos *100
    @property
    def n_alumnos(self):
        """
        Este metodo devuelve la cantidad de alumnos en el curso actualmente

        """
        return len(self.alumnos)

    def run(self):
        """
            Este metodo lanza la simulacion
            """
        print("----------- Bienvenido a programacion Avanzada ------------")

        self.poblar()
        self.secciones = len(self.profesores)
        a = 0
        for alumno in self.alumnos:
            a += alumno.confianza
        self.confianza_incial = a/len(self.alumnos)
        print ("[CURSO] Los alumnos se inscribieron a progra avanzada hay "
               "{} alumnos inscritos, {} secciones, {} "
               "ayudantes, {} profes, y un malvado coordinador".format(len(self.alumnos), self.secciones, len(self.ayudantes_docencia), len(self.profesores)))

        while self.dia <= 90:
            if self.dia in [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85]:
                self.comienzo_semana()
        print("[CURSO] Ha terminado el curso de programacion avanzada")

        grafico(self)
        estadisticas_personales(self)
        estadisticas_finales(self)

    def poblar(self):
        """
            Este metodo carga los integrantes de la simulacion desde el csv
            """
        with open("integrantes.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Rol:string"] == "Alumno":
                    r = random.choice([1,2,3])
                    if r == 1:
                        alumno = AlumnoArtistico(row["Nombre:string"])
                    elif r == 2:
                        alumno = AlumnoEficiente(row["Nombre:string"])
                    else:
                        alumno = AlumnoTeorico(row["Nombre:string"])
                    seccion = row["Sección:string"]
                    alumno.seccion = int(seccion)
                    alumno.confianza = random.uniform(self.confianzainf, self.confianzasup)
                    alumno.confianza_inicial = alumno.confianza
                    self.alumnos.append(alumno)

                elif row["Rol:string"] == "Profesor":
                    profesor = Profesor(row["Nombre:string"])
                    profesor.seccion = int(row["Sección:string"])
                    self.profesores.append(profesor)
                elif row["Rol:string"] == "Docencia":
                    ayudante = Ayudante_Docencia(row["Nombre:string"])
                    self.ayudantes_docencia.append(ayudante)
                elif row["Rol:string"] == "Tareas":
                    ayudante = Ayudante_Tareas(row["Nombre:string"])
                    self.ayudantes_tareas.append(ayudante)

    def comienzo_semana(self):
        """
            Este metodo corresponde al evento cuando pasa una semana, define cual es la materia de la semana,
            calcula las horas que trabajara cada alumno durante la semana
            """
        self.semana += 1
        self.control_semana = False
        self.tarea_semana = False
        if self.dia == 85:
            self.dia = 88
            self.materias.popleft()
            self.subir_tarea()
        else:
            if self.dia != 1:
                self.materias.popleft()
            materia = self.materias[0]
            for alumno in self.alumnos:
                if self.semana - 2 == alumno.visita_anterior[0]:
                    alumno.visita_anterior = [0, False]
                alumno.calcular_horas_semanas()
                alumno.nivel_original()
                if self.dia != 1:
                    alumno.actualizar_nivel_programacion()
            print("[Simulacion] Comienza la semana {}, la materia de esta semana es {}".format(self.semana, materia))
            if self.dia != 85:
                self.ayudantia()

    def visita_profesor(self):
        visitas = []
        for alumno in self.alumnos:
            if alumno.promedio < 4 and alumno.visita_anterior[1] == False:
                alumno.visita_anterior = [self.semana, True]
                visitas.append(alumno)
            elif alumno.visita_anterior[1] == True:
                r = random.random()
                if r < self.probprof:
                    alumno.visita_anterior = [self.semana, True]
                    visitas.append(alumno)
        alumnos = 0
        for i in range(10*self.secciones):
            if len(visitas) == 0:
                break
            alumno = random.choice(visitas)
            index = visitas.index(alumno)
            visitas.pop(index)
            alumno.nivel_programacion += alumno.nivel_programacion * 0.08
            alumnos += 1
        print("[PROFESOR] {} alumnos visitaron a sus profesores la semana {}".format(alumnos, self.semana))

    def ayudantia(self):
        """
            Este metodo corresponde al evento de la ayudantia
            """
        self.dia += 1
        self.visita_profesor()
        lista = self.ayudantes_docencia
        ayudante1 = random.choice(lista)
        ayudante2 = ayudante1
        while ayudante2 == ayudante1:
            ayudante2 = random.choice(lista)

        materia = self.materias[0]
        if (materia in ayudante1.materias) or (materia in ayudante2.materias):
            for alumno in self.alumnos:
                alumno.aumento_semanal += 0.1
        print("[Ayudantia] Los ayudantes {}, {} realizaron"
              " la ayudantia de {} la semana {}".format(ayudante1.nombre, ayudante2.nombre, materia, self.semana))
        self.catedra()

    def reunion_actividad(self):
        """
            Este metodo realiza el evento de definicion de la dificultad de la actividad
            """
        self.dia += 1
        materia = self.materias[0]
        dificultad = Dificultad(materia)
        exigencia = 7 + (random.randint(1, 5)) / dificultad
        self.exigencia_actividad = exigencia
        print("[Ayudantes de Docencia] Se definio el nivel de"
              " exigencia para la actividad de {} en {}".format(materia, exigencia))
        self.realizacion_actividad()
        self.subir_tarea()

    def realizacion_actividad(self):
        """
            Este metodo realiza el evento de la actividad.
            """
        if self.controles < 5:
            if self.controles == 0:
                r = random.randint(0, 1)
                if r == 1:
                    self.realizacion_control()
                else:
                    print("[ACTIVIDAD] No hay control sorpresa la semana {}".format(self.semana))
            elif self.semana - self.controles_grafico[-1][0] != 1:
                r = random.randint(0, 1)
                if r == 1:
                    self.realizacion_control()
                else:
                    print("[ACTIVIDAD] No hay control sorpresa la semana {}".format(self.semana))
            else:
                print("[ACTIVIDAD] No hay control sorpresa la semana {}".format(self.semana))
        materia = self.materias[0]
        alumnos = [[] for i in range(self.secciones)]
        for alumno in self.alumnos:
            alumnos[alumno.seccion - 1].append(alumno)
        for i in alumnos:
            n_consultas_realizadas = 0
            consultas = []
            for alumno in i:
                nconsultas = round(random.triangular(1, 10, 3))
                for j in range(nconsultas):
                    consultas.append(alumno.name)
            while len(consultas) != 0 or n_consultas_realizadas > 600:
                alumno_aumenta = random.choice(consultas)
                index = consultas.index(alumno_aumenta)
                consultas.pop(index)
                for alumno in self.alumnos:
                    if alumno.name == alumno_aumenta:
                        alumno.aumento_semanal += 0.01
                        n_consultas_realizadas += 1
        lista = []
        for alumno in self.alumnos:
            alumno.actualizar_horas_dedicadas()
            alumno.calcular_manejo(materia)
            if materia == "oop":
                alumno.oop += alumno.oop*alumno.aumento_semanal
            elif materia == "herencia":
                alumno.herencia += alumno.herencia * alumno.aumento_semanal
            elif materia == "edd":
                alumno.edd += alumno.edd * alumno.aumento_semanal
            elif materia == "arbol":
                alumno.arbol += alumno.arbol * alumno.aumento_semanal
            elif materia == "funcional":
                alumno.funcional += alumno.funcional * alumno.aumento_semanal
            elif materia == "meta":
                alumno.meta += alumno.meta * alumno.aumento_semanal
            elif materia == "simulacion":
                alumno.simulacion += alumno.simulacion * alumno.aumento_semanal
            elif materia == "thred":
                alumno.thred += alumno.thred * alumno.aumento_semanal
            elif materia == "interfaz":
                alumno.interfaz += alumno.interfaz * alumno.aumento_semanal
            elif materia == "bytes":
                alumno.bytes += alumno.bytes * alumno.aumento_semanal
            elif materia == "network":
                alumno.network += alumno.network * alumno.aumento_semanal
            elif materia == "webservices":
                alumno.webservices += alumno.webservices * alumno.aumento_semanal
            progresopep = 0.7 * alumno.materia(materia) + 0.2 * alumno.nivel_programacion + 0.1 * alumno.confianza
            progresocontenido = 0.7 * alumno.materia(materia) + 0.2*alumno.nivel_programacion + 0.1*alumno.confianza
            progresofuncionalidad = 0.3*alumno.materia(materia) + 0.6*alumno.nivel_programacion + 0.1*alumno.confianza
            progresototal = 0.4*progresofuncionalidad + 0.4 * progresocontenido + 0.2 * progresopep
            nota = round(max((progresototal/self.exigencia_actividad) * 7, 1), 2)
            if nota > 7:
                nota = 7
            if (materia == "funcional" and isinstance(alumno, AlumnoEficiente)) or (materia == "thred" and isinstance(alumno, AlumnoEficiente)):
                nota = nota + 1
                if nota > 7:
                    nota = 7
            elif (materia == "interfaz" and isinstance(alumno, AlumnoArtistico)) or (materia == "webservices" and isinstance(alumno, AlumnoArtistico)):
                nota += + 1
                if nota > 7:
                    nota = 7
            elif materia == "meta" and isinstance(alumno, AlumnoArtistico):
                nota = nota + 1
                if nota > 7:
                    nota = 7
            nota_esp = nota_esperada(alumno.horas_dedicadas_a_contenidos, materia)
            alumno.notas_esperadas["Actividades"].append(nota_esp)
            a = (alumno.name, nota)
            lista.append(a)
        suma2 = 0
        for nota in lista:
            suma2 += nota[1]
        prom_actividades = suma2/len(self.alumnos)
        b = (self.semana, prom_actividades)
        self.actividades_grafico.append(b)
        self.notas["Actividades"].append(lista)
        print("[ACTIVIDAD] Se realizo la actividad de {} la semana {}".format(materia, self.semana))

    def realizacion_control(self):
        """
            Este metodo realiza el control semanal si es que hay control.
            """
        self.control_semana = True
        self.controles += 1
        lista = []
        materia = self.materias[0]
        exigencia = 7 + random.randint(1, 5)/Dificultad(materia)
        for alumno in self.alumnos:
            alumno.actualizar_horas_dedicadas()
            alumno.calcular_manejo(materia)
            if materia == "oop":
                alumno.oop += alumno.oop*alumno.aumento_semanal
            elif materia == "herencia":
                alumno.herencia += alumno.herencia * alumno.aumento_semanal
            elif materia == "edd":
                alumno.edd += alumno.edd * alumno.aumento_semanal
            elif materia == "arbol":
                alumno.arbol += alumno.arbol * alumno.aumento_semanal
            elif materia == "funcional":
                alumno.funcional += alumno.funcional * alumno.aumento_semanal
            elif materia == "meta":
                alumno.meta += alumno.meta * alumno.aumento_semanal
            elif materia == "simulacion":
                alumno.simulacion += alumno.simulacion * alumno.aumento_semanal
            elif materia == "thred":
                alumno.thred += alumno.thred * alumno.aumento_semanal
            elif materia == "interfaz":
                alumno.interfaz += alumno.interfaz * alumno.aumento_semanal
            elif materia == "bytes":
                alumno.bytes += alumno.bytes * alumno.aumento_semanal
            elif materia == "network":
                alumno.network += alumno.network * alumno.aumento_semanal
            elif materia == "webservices":
                alumno.webservices += alumno.webservices * alumno.aumento_semanal
            progresocontenido = 0.7 * alumno.materia(materia) + 0.05*alumno.nivel_programacion + 0.2*alumno.confianza
            progresofuncionalidad = 0.3*alumno.materia(materia) + 0.2*alumno.nivel_programacion + 0.5*alumno.confianza
            progresototal = 0.3*progresofuncionalidad + 0.7 * progresocontenido
            nota = round(max((progresototal/exigencia) * 7, 1), 2)
            if nota > 7:
                nota = 7
            a = (alumno.name, nota)
            lista.append(a)
            nota_esp = nota_esperada(alumno.horas_dedicadas_a_contenidos, materia)
            alumno.notas_esperadas["Controles"].append(nota_esp)
        suma2 = 0
        for nota in lista:
            suma2 += nota[1]
        prom_controles = suma2/len(self.alumnos)
        b = (self.semana, prom_controles)
        self.controles_grafico.append(b)
        self.notas["Controles"].append(lista)
        print("[CONTROL] {} alumnos realizaron el control sorpresa de {} la semana {}".format(len(self.alumnos), materia, self.semana))

    def catedra(self):
        """
            Este metodo realiza la catedra
            """
        self.dia += 1
        materia = self.materias[0]
        for alumno in self.alumnos:
            r = random.randint(0,1)
            if r == 1:
                alumno.aumento_semanal += 0.1
        print("[CATEDRA] Se realizo la catedra de {} la semana {}".format(materia, self.dia, self.semana))
        self.reunion_actividad()

    def entrega_tarea(self, exigencia):
        """
            Este metodo realiza la entrega de las tareas de los alumnos
            """
        lista = []
        materia1 = self.materias_tarea[0]
        materia2 = self.materias_tarea[1]
        for alumno in self.alumnos:
            progresopep = 0.5 * (alumno.horas_dedicadas_a_tareas) + 0.5 * alumno.nivel_programacion
            progresocontenido = 0.7 * ((alumno.materia(materia1) + alumno.materia(materia2))/2)\
                                + 0.1 * alumno.nivel_programacion + 0.2 * alumno.horas_dedicadas_a_tareas
            progresofuncionalidad = 0.5 * ((alumno.materia(materia1) + alumno.materia(materia2))/2) \
                                    + 0.1 * alumno.nivel_programacion + 0.4 * alumno.horas_dedicadas_a_tareas
            progresototal = 0.4 * progresocontenido + 0.4 * progresofuncionalidad + 0.2 * progresopep
            nota = round(max((progresototal/exigencia)*7, 1), 2)
            if nota > 7:
                nota = 7
            a = (alumno.name, nota)
            lista.append(a)
            nota_esp1 = nota_esperada(alumno.horas_dedicadas_a_contenidos, materia1)
            nota_esp2 = nota_esperada(alumno.horas_dedicadas_a_contenidos, materia2)
            nota_esp = (nota_esp1+nota_esp2)/2
            alumno.notas_esperadas["Tareas"].append(nota_esp)
        suma2 = 0
        for nota in lista:
            suma2 += nota[1]
        prom_tareas = suma2/len(self.alumnos)
        b = (self.semana, prom_tareas)
        self.tareas_grafico.append(b)
        self.tarea_semana = True
        self.notas["Tareas"].append(lista)
        print("[TAREA] {} alumnos entregaron la tarea {} la semana {}".format(len(self.alumnos), self.tareas, self.semana))
        if self.tareas == 6:
            self.realizacion_examen()

    def subir_tarea(self):
        """
            Este metodo realiza la subida de enunciado de la tarea
            """
        self.dia += 1
        if self.dia == 5:
            self.tareas += 1
            materia1 = self.materias[0]
            index = self.materias2.index(materia1)
            materia2 = self.materias2[index + 1]
            self.materias_tarea = [materia1, materia2]
            dificultad = (Dificultad(materia1) + Dificultad(materia2)) / 2
            self.exigencia_tarea = 7 + random.randint(1, 5) / dificultad
            self.next_tarea = self.dia + 14
            print("[TAREA] Se subio el enunciado de la tarea {} la semana {}, es de {} y {}".format(self.tareas, self.semana,
                                                                                                  materia1, materia2))
            self.dia += 3
            return
        if self.next_tarea == self.dia:
            self.entrega_tarea(self.exigencia_tarea)
            if len(self.materias) != 0:
                self.tareas += 1
                materia1 = self.materias[0]
                index = self.materias2.index(materia1)
                materia2 = self.materias2[index+1]
                self.materias_tarea = [materia1, materia2]
                dificultad = (Dificultad(materia1) + Dificultad(materia2))/2
                self.exigencia_tarea = 7 + random.randint(1, 5)/dificultad
                self.next_tarea = self.dia + 14
                print("[TAREA] Se subio el enunciado de la tarea  {} la semana {}, es de {} y {}".format(self.tareas, self.semana, materia1, materia2))
                self.publicacion_notas()
            else:
                self.publicacion_notas()
        else:
            self.publicacion_notas()

    def publicacion_notas(self):
        """
            Este metodo realiza la publicacion de notas de actividades, tareas y controles
            """
        control = False
        tarea = False
        self.dia += 2
        r = random.random()
        if r < 0:
            print("[COORDINADOR] Se atraso la entrega de las notas de esta semana! muahaha ")
        else:
            for alumno in self.alumnos:
                for j in self.notas["Actividades"][-1]:
                    if j[0] == alumno.name:
                        alumno.notas_obtenidas["Actividades"].append(j[1])
                        break
                if len(self.notas["Controles"]) != 0 and self.control_semana == True:
                    for h in self.notas["Controles"][-1]:
                        if h[0] == alumno.name:
                            alumno.notas_obtenidas["Controles"].append(h[1])
                            control = True
                            break
                if len(self.notas["Tareas"]) != 0 and self.tarea_semana == True:
                    for k in self.notas["Tareas"][-1]:
                        if k[0] == alumno.name:
                            alumno.notas_obtenidas["Tareas"].append(k[1])
                            tarea = True
                            break
                alumno.calcular_confianza(control, tarea)

        print("[NOTAS] Se publico la nota de la actividad {} la semana {}".format(len(self.notas["Actividades"]), self.semana))
        if self.control_semana:
            print("[NOTAS] Se publico la nota del control {} la semana {}".format(len(self.notas["Controles"]), self.semana))
        if self.tarea_semana:
            print("[NOTAS] Se publico la nota de la tarea {} la semana {}".format(len(self.notas["Tareas"]), self.semana))
        if len(self.notas["Actividades"]) == 4:
            self.bota_ramos()
        self.dia += 1

    def bota_ramos(self):
        """
            Este metodo realiza la bota de ramos tras la actividad nº 4
            """
        i = 0
        self.botados = []
        for alumno in self.alumnos:
            confianza = alumno.confianza
            suma = 0
            for nota in alumno.notas_obtenidas["Actividades"]:
                suma += nota
            for nota in alumno.notas_obtenidas["Controles"]:
                suma += nota
            for nota in alumno.notas_obtenidas["Tareas"]:
                suma += nota

            s = confianza*0.8 + suma*0.2
            if s <= 3:
                i += 1
                self.botados.append(alumno)

        for k in self.botados:
            index = self.alumnos.index(k)
            self.alumnos.pop(index)

        print("[BOTA DE RAMOS] {} alumnos han botado el curso la semana {}".format(i, self.semana))

    def realizacion_examen(self):
        """
            Este metodo realiza el examen para los alumnos. Tambien define su dificultad por los ayudantes
            """
        h = 0
        lista = []
        for i in self.actividades_grafico:
            semana = i[0]
            promedio_actividad = i[1]
            for j in self.controles_grafico:
                if j[0] == semana:
                    promedio_control = j[1]
                else:
                    promedio_control = 0
            for k in self.tareas_grafico:
                if k[0] == semana:
                    promedio_tarea = k[1]
                elif k[0] == semana + 1:
                    promedio_tarea = k[1]
                else:
                    promedio_tarea = 0
            if promedio_control == 0 and promedio_tarea != 0:
                promedio_materia = (promedio_actividad + promedio_tarea)/2
            elif promedio_tarea == 0 and promedio_control != 0:
                promedio_materia = (promedio_actividad+ promedio_control)/2
            elif promedio_tarea == 0 and promedio_control == 0:
                promedio_materia = promedio_actividad
            else:
                promedio_materia = (promedio_actividad + promedio_tarea + promedio_control)/3
            a = (self.materias2[h], promedio_materia)
            lista.append(a)
            h += 1

        materia1 = max(lista, key = lambda x: x[1])
        index = lista.index(materia1)
        materia1 = materia1[0]
        lista.pop(index)
        materia2 = max(lista, key =lambda x: x[1])
        index = lista.index(materia2)
        materia2 = materia2[0]
        lista.pop(index)
        materia3 = min(lista, key= lambda x: x[1])
        index = lista.index(materia3)
        lista.pop(index)
        materia3 = materia3[0]
        materia4 = min(lista, key=lambda x: x[1])
        index = lista.index(materia4)
        lista.pop(index)
        materia4 = materia4[0]
        materia5 = min(lista, key=lambda x: x[1])
        index = lista.index(materia5)
        lista.pop(index)
        materia5 = materia5[0]
        materia6 = min(lista, key=lambda x: x[1])
        index = lista.index(materia6)
        lista.pop(index)
        materia6 = materia6[0]
        materia7 = min(lista, key=lambda x: x[1])
        index = lista.index(materia7)
        lista.pop(index)
        materia7 = materia7[0]
        materia8 = min(lista, key=lambda x: x[1])
        index = lista.index(materia8)
        lista.pop(index)
        materia8 = materia8[0]
        materias = [materia1, materia2, materia3, materia4, materia5, materia6, materia7, materia8]
        for materia in materias:
            dificultad = Dificultad(materia)
            exigencia = random.randint(1,5)/dificultad + 7
            lista_notas = []
            for alumno in self.alumnos:
                progreso_contenido = 0.5 * alumno.materia(materia) + 0.1 * alumno.nivel_programacion + 0.4 * alumno.confianza
                progreso_funcionalidad = 0.3 * alumno.materia(materia) + 0.2 * alumno.nivel_programacion + 0.5 * alumno.confianza
                progreso_total = 0.3 * progreso_funcionalidad + 0.7 * progreso_contenido
                nota = round(max(progreso_total/exigencia * 7, 1),2)
                if isinstance(alumno, AlumnoTeorico):
                    nota += 1
                if nota > 7:
                    nota = 7
                alumno.notas_obtenidas["Examen"].append(nota)
                c = (alumno.name, nota)
                lista_notas.append(c)
            self.notas["Examen"].append(lista_notas)
        print("[Examen] {} alumos realizaron el examen la semana {}".format(self.n_alumnos, 13))
        print("[NOTAS] Se publico la nota del examen la semana {}".format(self.n_alumnos, 13))


if __name__ == "__main__":
    simulacion = Simulacion()
    simulacion.run()




