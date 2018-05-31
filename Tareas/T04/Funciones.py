import csv
import random

def Dificultad(materia):
    dic = {"oop":2,"herencia":2,"edd":3,"arbol":5,"funcional":7,
           "meta":10,"simulacion":7,"thred":9,
           "interfaz":1,"bytes":6,"network":6,"webservices":5}

    for k,v in dic.items():
        if k == materia:
            return v
        else:
            continue

    raise AssertionError("Materia no hayada!")

def leer_archivo(name):
    with open(str(name)+".csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def nota_esperada(horas, materia):
    if materia == "oop":
        if 0 <= horas <= 2:
            return round(random.uniform(1.1,3.9),2)
        elif 3 <= horas <= 4:
            return round(random.uniform(4.0, 5.9), 2)
        elif 5 <= horas <= 6:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "herencia":
        if 0 <= horas <= 3:
            return round(random.uniform(1.1, 3.9), 2)
        elif 4 <= horas <= 6:
            return round(random.uniform(4.0, 5.9), 2)
        elif 7 <= horas < 8:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "edd":
        if 0 <= horas <= 1:
            return round(random.uniform(1.1, 3.9), 2)
        elif 2 <= horas <= 4:
            return round(random.uniform(4.0, 5.9), 2)
        elif 5 <= horas <= 6:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "arbol":
        if 0 <= horas <= 2:
            return round(random.uniform(1.1, 3.9), 2)
        elif 3 <= horas <= 5:
            return round(random.uniform(4.0, 5.9), 2)
        elif 6 <= horas <= 7:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "funcional":
        if 0 <= horas <= 3:
            return round(random.uniform(1.1, 3.9), 2)
        elif 4 <= horas <= 7:
            return round(random.uniform(4.0, 5.9), 2)
        elif 7 <= horas < 8:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "meta":
        if 0 <= horas <= 4:
            return round(random.uniform(1.1, 3.9), 2)
        elif 5 <= horas <= 7:
            return round(random.uniform(4.0, 5.9), 2)
        elif 8 <= horas <= 9:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "simulacion":
        if 0 <= horas <= 3:
            return round(random.uniform(1.1, 3.9), 2)
        elif 4 <= horas <= 6:
            return round(random.uniform(4.0, 5.9), 2)
        elif 7 <= horas <= 8:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "thred":
        if 0 <= horas <= 2:
            return round(random.uniform(1.1, 3.9), 2)
        elif 3 <= horas <= 5:
            return round(random.uniform(4.0, 5.9), 2)
        elif 6 <= horas <= 7:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7

    elif materia == "interfaz":
        if 0 <= horas <= 1:
            return round(random.uniform(1.1, 3.9), 2)
        elif 2 <= horas <= 4:
            return round(random.uniform(4.0, 5.9), 2)
        elif 5 <= horas <= 6:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7

    elif materia == "bytes":
        if 0 <= horas <= 4:
            return round(random.uniform(1.1, 3.9), 2)
        elif 5 <= horas <= 7:
            return round(random.uniform(4.0, 5.9), 2)
        elif 8 <= horas <= 9:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7
    elif materia == "network":
        if 0 <= horas <= 2:
            return round(random.uniform(1.1, 3.9), 2)
        elif 3 <= horas <= 5:
            return round(random.uniform(4.0, 5.9), 2)
        elif 6 <= horas <= 7:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7

    elif materia == "webservices":
        if 0 <= horas <= 2:
            return round(random.uniform(1.1, 3.9), 2)
        elif 3 <= horas <= 7:
            return round(random.uniform(4.0, 5.9), 2)
        elif 7 <= horas < 8:
            return round(random.uniform(6.0, 6.9), 2)
        else:
            return 7


def leer_escenario():
    with open("escenarios.csv", "r") as file:
        escenarios = [[] for __ in range(len(file.readline().split(",")))]
        for lines in file:
            linea = lines.split(",")
            for i in range(1,len(linea)):
                escenarios[i-1].append(linea[i])
        return escenarios


if __name__ == "__main__":
    leer_escenario()
