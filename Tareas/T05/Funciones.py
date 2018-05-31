from math import sqrt

def checkdistance(uno, dos):
    vector = [uno.position[0] - dos.position[0], uno.position[1] - dos.position[1]]
    distancia = sqrt(vector[0] ** 2 + vector[1] ** 2)
    return distancia

def direccion(origen, destino):
    destino1 = destino
    origen1 = origen
    destino = [destino[0] - origen[0], destino[1] - origen[1]]
    if destino[1] > destino[0]/2 and destino[1] < 2*destino[0]:
        return "diag4"
    elif destino[1] > 2*destino[0] and destino[1] < -2*destino[0]:
        if destino[1] > 60:
            return "diag3"
        else:
            return "izq"

    elif destino[1] < 0 and destino[1]<destino[0]/2:
        if destino[0] < 0:
            return "diag2"
        elif destino[1] < -destino[0]/2:
            return "arriba"
        else:
            return "diag1"
    elif destino[1] > destino[0]*2 and destino[1] > 0:
        return "abajo"

    elif destino[1] < destino[0]*2:
        return "derecha"
    else:
        return "diag1"


