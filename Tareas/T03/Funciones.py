# Este modulo se encarga de generar las funciones necesarias
from functools import reduce
import math


def normal(x, mu, sigma):
    valor = 1/(math.sqrt(2*math.pi*(sigma**2)))*math.exp(-0.5*((x-mu)/sigma)**2)
    return valor


def exponencial(x, nu):
    valor = nu * (math.exp(-nu*x))
    return valor


def gamma(x, nu, k):
    valor = ((nu**k)/factorial(k-1))*x**(k-1)*math.exp(-nu*x)
    return valor


def decimal_range(inicio, fin, step):
    r = inicio
    while r < fin:
        yield r
        r += step


def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, n+1))


def abrir_archivo(nombre):
    archivo = open(str(nombre)+".csv", "r")
    lista = [x.rstrip().split(";") for x in archivo]
    lista[0] = [x.split(":")[0] for x in lista[0]]
    return lista


if __name__ == "__main__":
    pass
