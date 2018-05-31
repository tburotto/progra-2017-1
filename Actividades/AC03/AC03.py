
class Camion:
    def __init__(self, capacidad_maxima, urgencia):
        self.capacidad_maxima = capacidad_maxima
        self.urgencia = urgencia
        self.productos = {}
        self.peso_actual = 0

    def agregarproductos(self, producto):
        tipo = producto[0]
        if self.peso_actual + producto[2] <= self.capacidad_maxima:
            self.productos[tipo].append(producto)
            self.peso_actual += producto[2]
            return True
        else:
            print("El camion esta lleno")
            return False

    def __str__(self):
        for k,v in self.productos.items():
            print(k +":"+ len(v))

class Centros:
    def __init__(self, productos):
        self.fila = []
        self.bodega = {}
        self.productos = productos
        for k in productos:
            if k[0] in self.bodega:
                self.bodega[k[0]].append(k)
            else:
                self.bodega[k[0]] = [k]

    def recibir_camion(self,camion):
        if len(self.fila) == 0:
            self.fila.append(camion)
        else:
            i = 0
            for k in self.fila:
                if k.urgencia <= camion.urgencia:
                    self.fila.insert(i, camion)
                    break

    def rellenar_camion(self):
        peso = 0
        posk = ""
        posj = 0
        objeto = ""
        for k in self.bodega.values():
            for j in k:
                posj = posj + 1
                if j[2] >= peso:
                    peso = j[2]
                    objeto = j
                    posk = k
                    posjfin = posj

        self.bodega[posk].pop(posjfin)
        if self.fila[0].agregarproductos(objeto):
            return True
        else:
            return False
                    
    def enviar_camion(self):
        if self.rellenar_camion(self.fila[0]) == False:
            self.fila.pop(0)

        else:
            pass

    def mostrar_productos_por(self, tipo):
        dic = {}
        for k in self.bodega:
            for j in k:
                if j[1] not in dic:
                    dic[j[1]] = 1
                else:
                    dic[j[1]] += 1

        for k, v in self.productos.items():
            for h, u in dic.items():
                print(k+":"+h+"u")
            
    def recibir_donacion(self,producto):


        self.bodega[producto[0]].append((producto[1],producto[2]))


camiones =[]
with open("camiones.txt") as f:
    lista = f.readlines()
    for k in lista:
        j = k.split(",")
        camiones.append(j)

lista_camiones = []
for k in camiones:
    camion_nuevo = Camion(k[0],k[1].replace("\\n", ""))
    lista_camiones.append(camion_nuevo)

productos = []

with open("productos.txt") as f:
    lista = f.readlines()
    for k in lista:
        j = k.split(",")
        productos.append(j)

lista_productos = []
for k in productos:
    producto_nuevo = (k[0], k[1], int(k[2]))
    lista_productos.append(producto_nuevo)

centro = Centros(lista_productos)

print(len(centro.bodega))