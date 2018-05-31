import matplotlib.pyplot as plt

def grafico(simulacion):
    semanas_controles = []
    notas_controles = []
    semanas_tareas = []
    notas_tareas = []
    semanas_actividades= []
    notas_actividades = []
    for i in simulacion.controles_grafico:
        notas_controles.append(i[0])
        semanas_controles.append(i[1])

    for i in simulacion.tareas_grafico:
        notas_tareas.append(i[0])
        semanas_tareas.append(i[1])

    for i in simulacion.actividades_grafico:
        notas_actividades.append(i[0])
        semanas_actividades.append(i[1])

    plt.plot(notas_controles, semanas_controles, label="controles")
    plt.plot(notas_tareas, semanas_tareas, label="tareas")
    plt.plot(notas_actividades, semanas_actividades, label="actividades")
    plt.xlabel("Semanas")
    plt.ylabel("Notas")
    plt.title("Notas en función de la semana")
    plt.legend()
    plt.show()


def estadisticas_personales(simulacion):
    while True:
        print("----- Estadisticas personales ------")
        i = str(input("Nombre de alumno a consultar (ingresa nombre o salir para salir) : "))
        if i == "salir":
            break
        else:
            for alumno in simulacion.alumnos:
                if alumno.name == i:
                    print("---- Cualidades -----")
                    print("Nivel de programacion : {}, Manejo de "
                          "contenidos : {}, Confianza: "
                          "{}".format(alumno.nivel_programacion, alumno.manejo, alumno.confianza))
                    print("---- Notas ----")
                    i = 1
                    for controles in alumno.notas_obtenidas["Controles"]:
                        print("Control {}: {}".format(i, controles))
                        i += 1
                    i = 1
                    for tareas in alumno.notas_obtenidas["Tareas"]:
                        print("Tarea {}: {}".format(i, tareas))
                        i += 1
                    i = 1
                    for actividades in alumno.notas_obtenidas["Actividades"]:
                        print("Actividad {}: {}".format(i, actividades))
                        i += 1
                    i = 1
                    for preguntas in alumno.notas_obtenidas["Examen"]:
                        print("Pregunta Examen {}: {}".format(i, preguntas))
                        i += 1

def estadisticas_finales(simulacion):
    a = 0
    for alumno in simulacion.alumnos:
        a += alumno.confianza
    confianza = a/len(simulacion.alumnos)
    print("------ Estadisticas Finales -------")
    print("Alumnos que botaron el ramo : {}".format(len(simulacion.botados)))
    print("Confianza inicial : {} - Confianza final : {}".format(simulacion.confianza_incial, confianza))
    promedio_mes1 = 0
    promedio_mes2 = 0
    promedio_mes3 = 0
    i = 0
    j = 0
    k = 0
    for nota in simulacion.actividades_grafico:
        if nota[0] in [1, 2, 3, 4]:
            mes = 1
            promedio_mes1 += nota[1]
            i += 1
        elif nota[0] in [5, 6, 7, 8]:
            mes = 2
            promedio_mes2 += nota[1]
            j += 1
        else:
            mes = 3
            promedio_mes3 += nota[1]
            k += 1
    promedio_mes1_actividad = promedio_mes1 / i
    promedio_mes2_actividad = promedio_mes2 / j
    promedio_mes3_actividad = promedio_mes3 / k
    i = 0
    j = 0
    k = 0

    for nota in simulacion.tareas_grafico:
        if nota[0] in [1, 2, 3, 4]:
            mes = 1
            promedio_mes1 += nota[1]
            i += 1
        elif nota[0] in [5, 6, 7, 8]:
            mes = 2
            promedio_mes2 += nota[1]
            j += 1
        else:
            mes = 3
            promedio_mes3 += nota[1]
            k += 1
    promedio_mes1_tarea = promedio_mes1 / i
    promedio_mes2_tarea = promedio_mes2 / j
    promedio_mes3_tarea = promedio_mes3 / k
    suma = 0
    examen = 0
    for pregunta in simulacion.notas["Examen"]:
        for notas in pregunta:
            suma += notas[1]
        examen += suma
        suma = 0
    promedio_examen = examen/8
    promedio_mes1 = promedio_mes1_actividad * 0.15 + promedio_mes1_tarea * 0.35 + 0.5
    promedio_mes2 = promedio_mes2_actividad * 0.15 + promedio_mes2_tarea * 0.35 + 0.5
    promedio_mes3 = promedio_mes3_actividad * 0.15 + promedio_mes3_tarea * 0.35 + promedio_examen * 0.5

    if max(promedio_mes1,promedio_mes2,promedio_mes3) == promedio_mes1:
        mes = 1
    elif max(promedio_mes1,promedio_mes2,promedio_mes3) == promedio_mes2:
        mes = 2
    else:
        mes = 3

    print("El mes con mayor aprobacion : {}".format(mes))
    j = 1
    for tareas in simulacion.notas["Tareas"]:
        i = 0
        for notas in tareas:
            if notas[1] > 4.0:
                i += 1
        print("Tarea {} - Aprobacion : {} % - Reprobacion : {} %".format(j, (i / len(tareas) * 100),
                                                                       100 - (i / len(tareas) * 100)))
        j += 1
    j = 1
    for actividades in simulacion.notas["Actividades"]:
        i = 0
        for notas in actividades:
            if notas[1] > 4.0:
                i += 1
        print("Actividad {} - Aprobacion : {} % - Reprobacion : {} %".format(j, (i / len(actividades) * 100),
                                                                       100 - (i / len(actividades) * 100)))
        j += 1
    j = 1
    for preguntas in simulacion.notas["Examen"]:
        i = 0
        for notas in preguntas:
            if notas[1] > 4.0:
                i += 1
        print("Pregunta Examen {} - Aprobacion : {} % - Reprobacion : {} %".format(j, (i / len(preguntas) * 100),
                                                                       100 - (i / len(preguntas) * 100)))
        j += 1




