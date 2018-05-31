# PRIMERA PARTE: Estructura basica


class Nodo:
    def __init__(self, valor):
        self.next = None
        self.valor = valor


class Lista_Ligada:
    def __init__(self, *args):
        self.cola = None
        self.cabeza = None
        for arg in args:
            self.append(arg)

    def append(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.next = Nodo(valor)
            self.cola = self.cola.next

    def __getitem__(self, item):
        nodo = self.cabeza
        for i in range(item):
            if nodo:
                nodo = nodo.next
            else:
                raise IndexError

        if not nodo:
            raise IndexError
        else:
            return nodo.valor

    def __in__(self, valor):
        nodo = self.cabeza
        while nodo:
            if nodo == valor:
                return True
            else:
                nodo = nodo.next
                if not nodo:
                    return False

    def __repr__(self):
        nodo = self.cabeza
        linea = “[“		
        while nodo:
            linea += str(nodo.valor)+", "
            nodo = nodo.next
        linea = linea.rstrip(", ") + "]"
        return linea

# SEGUNDA PARTE: Clase Isla


class Isla:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = Lista_Ligada()

    def agregar_conexion(self, otra_isla):
        self.conexiones.append(otra_isla)

    def __repr__(self):
        s = str(self.nombre)
        return s


# TERCERA PARTE: Clase Archipielago
class Archipielago:
    def __init__(self, archivo):
        self.islas = Lista_Ligada()
        self.conexiones = Lista_Ligada()
        self.archivo = archivo
        self.construir()

    def agregar_isla(self, isla):
        self.islas.append(isla)  ###

    def agregar_conexion(self, nombre_origen, nombre_destino):
        i = 0
        for nombre in Lista_Ligada(nombre_origen, nombre_destino):
            isla_repetida = False
            for isla in self.islas:
                if isla.nombre == nombre:
                    if i == 0:
                        isla_origen = isla
                    else:
                        isla_destino = isla
                    isla_repetida = True
                    break
            i += 1
            if not isla_repetida:
                if i == 1:
                    isla_origen = Isla(nombre)
                    self.agregar_isla(isla_origen)
                else:
                    isla_destino = Isla(nombre)
                    self.agregar_isla(isla_destino)

        isla_origen.agregar_conexion(isla_destino)

    def construir(self):
        arch = open(self.archivo, "r")
        while True:
            linea = arch.readline()
            if not linea:
                break
            nombre_isla_origen = ""
            nombre_isla_destino = ""
            escribiendo_en = "origen"
            for char in linea:
                if char == ",":
                    escribiendo_en = "destino"
                    continue
                if escribiendo_en == "origen":
                    nombre_isla_origen += char
                else:
                    nombre_isla_destino += char

            nombre_isla_destino = nombre_isla_destino.strip("\n")
            self.agregar_conexion(nombre_isla_origen, nombre_isla_destino)

    def __repr__(self):
        s = ""
        for i in self.islas:
            s += "Isla: "+str(i.nombre) + ", Conexiones: "+ str(i.conexiones)+"\n"
        return s

    def propagacion(self, nombre_origen):
        islas_conectadas= Lista_Ligada()
        return self.propagacion2(nombre_origen, islas_conectadas)

    def propagacion2(self, nombre_origen, islas_conectadas):
        for i in self.islas:
            if i.nombre == nombre_origen:
                isla= i
                break
        islas_conectadas.append(isla)
        for conexion in isla.conexiones:
            if conexion not in islas_conectadas:
                self.propagacion2(conexion.nombre, islas_conectadas)

        return islas_conectadas

if __name__ == '__main__':
    # No modificar desde esta linea
    # (puedes comentar lo que no este funcionando aun)
    arch = Archipielago("mapa.txt") # Instancia y construye
    print(arch) # Imprime el Archipielago de una forma que se pueda entender
    print(arch.propagacion("Perresus"))
    print(arch.propagacion("Pasesterot"))
    print(arch.propagacion("Cartonat"))
    print(arch.propagacion("Womeston"))
