from functools import reduce
import math
import matplotlib.pyplot as plt
import numpy as np
import Funciones
variables = []

# lector


def lector(lista):
    if lista[0] == "asignar":
        return asignar(lista)
    elif lista[0] == "PROM":
        return promedio(lista)
    elif lista[0] == "LEN":
        return len1(lista)
    elif lista[0] == "MEDIAN":
        return mediana(lista)
    elif lista[0] == "DESV":
        return desv(lista)
    elif lista[0] == "VAR":
        return var(lista)
    elif lista[0] == "graficar":
        return graficar(lista)
    elif lista[0] == "comparar":
        return comparar(lista)
    elif lista[0] == "comparar_columna":
        return comparar_columnas(lista)
    elif lista[0] == "do_if":
        return do_if(lista)
    elif lista[0] == "crear_funcion":
        return crear_funcion(lista)
    elif lista[0] == "extraer_columna":
        return extraer_columna(lista)
    elif lista[0] == "evaluar":
        return evaluar(lista)
    elif lista[0] == "filtrar":
        return filtrar(lista)
    elif lista[0] == "operar":
        return operar(lista)
    else:
        return "ERROR, comando no encontrado"
# Decoradores


def decorar_consultas_asignacion(f):
    def decorador(data):
        lista1 = []
        global variables
        if isinstance(data, list):
            lista1 = [x for x in variables if x[0] in data]
        if len(lista1) > 0:
            datos = lista1[0]
            i = [i for i in range(0, len(data)) if data[i] == datos[0]]
            if len(i) >= 2:
                data[i[0]] = datos[1]
                data[i[1]] = datos[1]
            else:
                data[i[0]] = datos[1]
            return f(data)
        else:
            return f(data)
    return decorador


def decorar_consultas_anidacion(f):
    def decorador1(data):
        if isinstance(data, list):
            for a in data:
                if isinstance(a, list):
                    if isinstance(a[0], str):
                        indice = data.index(a)
                        data[indice] = lector(a)
            return f(data)
        else:
            return f(data)
    return decorador1

# COMANDOS BASICOS

# Grafico


@decorar_consultas_asignacion
def graficar(data):
    if isinstance(data, list):
        if data[0] != "graficar":
            return data
        else:
            if isinstance(data[2], str):
                if data[2] == "numerico":
                    y = data[1]
                    x = [i for i in range(0, len(y))]
                    plot = plt.plot(x, y)
                    plt.show()
                    return "Graficado!"
                elif data[2] == "normalizado":
                    y = data[1]
                    suma = reduce(lambda h, k: h+k, y)
                    x = [i/suma for i in range(0, len(y))]
                    plot = plt.plot(x, y)
                    plt.show()
                    return "Graficado!"
                elif "rango" in data[2]:
                    rango = data[2].replace("rango:", "")
                    datos = rango.split(",")
                    step = float(datos[2])
                    x = np.arange(float(datos[0]), float(datos[1]), step)
                    y = data[1]
                    plot = plt.plot(x, y)
                    plt.show()
                    return "Graficado!"
                else:
                    return data

            else:
                x = data[1]
                y = data[2]
                plot = plt.plot(x, y)
                plt.show()
                return "Graficado!"
    else:
        return data


@decorar_consultas_anidacion
def asignar(data):
    if isinstance(data, list):
        if data[0] != "asignar":
            return data
        else:
            global variables
            variables.append([data[1], data[2]])
            return "Valor asignado"
    else:
        return data
# Comandos que retornan un valor


@decorar_consultas_asignacion
def promedio(data):
    try:
        if isinstance(data, list):
            if data[0] == "PROM":
                suma = reduce(lambda x, y: (x + y), data[1])
                promedio = suma / len(data[1])
                return promedio

            else:
                return data
        else:
            return data
    except Exception:
        return "Error, el segundo argumento debe ser una lista o variable"


@decorar_consultas_asignacion
def len1(data):
    try:
        if isinstance(data, list):
            if data[0] != "LEN":
                return data
            else:
                if isinstance(data[1], str):
                    raise TypeError
                else:
                    largo = len(data[1])
                    return largo
        else:
            return data
    except TypeError:
        return "Error, el segundo argumento debe ser una lista o variable"


@decorar_consultas_asignacion
def mediana(data):
    try:
        if isinstance(data, list):
            if data[0] != "MEDIAN":
                return data
            else:
                if len(data[1]) % 2 == 0:
                    dato1 = data[1][int((len(data[1])/2))]
                    dato2 = data[1][int((len(data[1])/2)-1)]
                    median = (dato1+dato2)/2
                else:
                    median = data[1][int((len(data[1])-1)/2)]
            return median
        else:
            return data
    except TypeError:
        return "Error, el segundo argumento debe ser una lista o variable"


@decorar_consultas_asignacion
def desv(data):
    try:
        if isinstance(data, list):
            if data[0] != "DESV":
                return data
            else:
                suma = [(x - promedio(["PROM", data[1]]))**2 for x in data[1]]
                suma = reduce(lambda x, y: x+y, suma)
                desvia = suma/(len(data[1])-1)
                desvia = math.sqrt(desvia)
                return desvia

        else:
            return data
    except TypeError:
        return "Error, el segundo argumento debe ser una lista o variable"


@decorar_consultas_asignacion
def var(data):
    try:
        if isinstance(data, list):
            if data[0] != "VAR":
                return data
            else:
                desvia = desv(["DESV", data[1]])
                vari = desvia ** 2
                return vari
        else:
            return data
    except TypeError:
        return "Error, el segundo argumento debe ser una lista o variable"


# comandos que retornan un booleano

@decorar_consultas_anidacion
@decorar_consultas_asignacion
def comparar(data):
    try:
        if isinstance(data, list):
            if data[0] != "comparar":
                return data
            else:
                if (isinstance(data[1], int) or isinstance(data[1], float)) \
                        and (isinstance(data[3], int) or isinstance(data[3], float)):
                    if data[2] == ">":
                        if data[1] > data[3]:
                            return True
                        else:
                            return False
                    elif data[2] == "<":
                        if data[1] < data[3]:
                            return True
                        else:
                            return False
                    elif data[2] == ">=":
                        if data[1] == data[3] or data[1] > data[3]:
                            return True
                        else:
                            return False
                    elif data[2] == "<=":
                        if data[1] == data[3] or data[1] < data[3]:
                            return True
                        else:
                            return False
                    elif data[2] == "==":
                        if data[1] == data[3]:
                            return True
                        else:
                            return False
                    elif data[2] == "!=":
                        if data[1] != data[3]:
                            return True
                        else:
                            return False
                    else:
                        raise Exception("Simbolo incorrecto!")
                else:
                    return data
        else:
            return data

    except Exception as err:
        if err == TypeError:
            return "Error, el segundo argumento debe ser un numero o varible"
        else:
            return "Simbolo mal ingresado"


@decorar_consultas_asignacion
def comparar_columnas(data):
    try:
        if isinstance(data, list):
            if data[0] != "comparar_columna":
                return data
            else:
                columna1 = data[1]
                columna2 = data[4]
                simbolo = data[2]
                operacion = data[3]
                if not isinstance(columna1, list) or not isinstance(columna2, list):
                    raise Exception("Las columnas no fueron ingresadas correctamente!")
                else:
                    columna1_o = lector([operacion, columna1])
                    columna2_o = lector([operacion, columna2])
                    return comparar(["comparar", columna1_o, simbolo, columna2_o])
        else:
            return data
    except Exception:
        return "Hubo un error"


@decorar_consultas_asignacion
def do_if(data):
    try:
        if isinstance(data, list):
            if data[0] != "do_if":
                return data
            else:
                consulta1 = data[1]
                consulta2 = data[2]
                consulta3 = data[3]
                if isinstance(consulta1, list) and isinstance(consulta2, list) and isinstance(consulta3, list):
                    consulta2o = lector(consulta2)
                    if consulta2o == True:
                        consulta1o = lector(consulta1)
                        return consulta1o
                    else:
                        consulta3o = lector(consulta3)
                        return consulta3o
        else:
            return data
    except Exception:
        return "Algo fallo"


@decorar_consultas_asignacion
def crear_funcion(data):
    if isinstance(data, list):
        if data[0] != "crear_funcion":
            return data
        else:
            funcion = data[1]
            if funcion == "normal":
                mu = data[2]
                sigma = data[3]
                return ["normal", mu, sigma]
            elif funcion == "exponencial":
                nu = data[2]
                return ["exponencial", nu]
            elif funcion == "gamma":
                nu = data[2]
                k = data[3]
                return ["gamma", nu, k]
            else:
                raise Exception("Funcion incorrecta!")

# Comandos que retornan un conjunto de datos


@decorar_consultas_asignacion
def filtrar(data):
    try:
        if isinstance(data, list):
            if data[0] != "filtrar":
                return data
            else:
                lista = [x for x in data[1] if comparar(["comparar", x, data[2], data[3]]) == True]
                return lista
        else:
            return data
    except Exception:
        return "ERROR datos mal ingresados"


@decorar_consultas_asignacion
def operar(data):
    try:
        if isinstance(data, list):
            if data[0] != "operar":
                return data
            else:
                columna = data[1]
                simbolo = data[2]
                valor = data[3]
                if simbolo == "+":
                    lista_retorno = [x+valor for x in columna]
                    return lista_retorno
                elif simbolo == "-":
                    lista_retorno = [x - valor for x in columna]
                    return lista_retorno
                elif simbolo == "*":
                    lista_retorno = [x*valor for x in columna]
                    return lista_retorno
                elif simbolo == "**":
                    lista_retorno = [x**valor for x in columna]
                    return lista_retorno
                elif simbolo == "/":
                    lista_retorno = [x/valor for x in columna]
                    return lista_retorno
                else:
                    raise Exception("Simbolo incorrecto!")
    except Exception:
        return "ERROR DE SINTAX O ERROR MATEMATICO"


@decorar_consultas_anidacion
@decorar_consultas_asignacion
def evaluar(data):
    try:
        if isinstance(data, list):
            if data[0] != "evaluar":
                return data
            else:
                funcion = data[1]
                inicio = data[2]
                final = data[3]
                intervalo = data[4]
                if funcion[0] == "normal":
                    mu = funcion[1]
                    sigma = funcion[2]
                    lista = [Funciones.normal(x, mu, sigma) for x in Funciones.decimal_range(inicio, final, intervalo)]
                    return lista
                elif funcion[0] == "exponencial":
                    nu = data[1]
                    lista = [Funciones.exponencial(x, nu) for x in Funciones.decimal_range(inicio, final, intervalo)]
                    return lista
                elif funcion[0] == "gamma":
                    nu = funcion[1]
                    k = funcion[2]
                    lista = [Funciones.gamma(x, nu, k) for x in Funciones.decimal_range(inicio, final, intervalo)]
                    return lista
                else:
                    raise Exception("ERROR: funcion mal definida")

        else:
            return data
    except Exception:
        return "ERROR FUNCION MAL DEFINIDA"


@decorar_consultas_asignacion
def extraer_columna(data):
    try:
        if isinstance(data, list):
            if data[0] != "extraer_columna":
                return data
            else:
                archivo = data[1]
                columna = data[2]
                lista_archivo = Funciones.abrir_archivo(archivo)
                if columna in lista_archivo[0]:
                    indice = lista_archivo[0].index(columna)
                    lista = [x[indice] for x in lista_archivo]
                    return lista
                else:
                    raise Exception("columna no hayada en archivo")
    except Exception:
        return "ERROR: datos mal ingresados"


if __name__ == "__main__":
    pass
