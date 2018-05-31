from Estructuras import *

class Lector:
    def __init__(self):
        pass

    def abrir_population(self, archivo = "population.csv"):
        lista1 = ListaLigada()
        f = open(archivo, "r")
        for line in f:
            w = ""
            lista2 = ListaLigada()
            for letra in line:
                w += letra
                if letra == ",":
                    w = w.rstrip(",")
                    lista2.append(w)
                    w = ""
                elif letra == "\n":
                    w = w.strip("\n")
                    lista2.append(w)
                    w = ""

            lista1.append(lista2)
        f.close()
        return lista1

    def abrir_airports(self):
        archivo = "airports.csv"
        lista1 = ListaLigada()
        f = open(archivo, "r")
        for line in f:
            w = ""
            for letra in line:
                w += letra
                if letra == ",":
                    w = w.rstrip(",")
                    lista1.append(w)
                    w = ""

        f.close()
        return lista1

    def abrir_borders(self):
        archivo = "borders.csv"
        dictborders = Dict()
        f = open(archivo, "r")
        s = ""
        i = 0
        for line in f:
            i += 1
            if i == 1:
                continue
            w = ""
            for letra in line:
                w += letra
                if letra == ";":
                    w = w.rstrip(";")
                    s = w
                    if not dictborders.isin(w):
                        dictborders.append(Key(w, ListaLigada()))
                    w = ""
                elif letra == "\n":
                    w = w.strip("\n")
                    dictborders[s].append(w)


        f.close()
        return dictborders

    def random_airports(self):
        f = open("random_airports.csv", "r")
        dict_airports_borders = Dict()
        s = ""
        i = 0
        for line in f:
            i += 1
            if i == 1:
                continue
            w = ""
            for letra in line:
                w += letra
                if letra == ",":
                    w = w.rstrip(",")
                    s = w
                    if not dict_airports_borders.isin(w):
                        dict_airports_borders.append(Key(w, ListaLigada()))
                    w = ""
                elif letra == "\n":
                    w = w.strip("\n")
                    dict_airports_borders[s].append(w)

        return dict_airports_borders

    def guardar_juego(self, pandemia):
        nombre = pandemia.name
        file = open("paises_"+str(nombre)+".csv", "w")
        lista_paises = pandemia.paises
        file.write("Nombre;dias_infectado;infectados;muertos;aeropuerto;borders;borders_aeropuerto;infeccion;cura;avance de cura\n")
        for pais in lista_paises:
            file.write(str(pais.nodo_valor.nombre)+";"+str(pais.nodo_valor.dias_infectado)+";"
                       +str(pais.nodo_valor.infectados)+";"+str(pais.nodo_valor.muertos)+";"
                       + str(pais.nodo_valor.aeropuerto) + ";"+str(pais.nodo_valor.borders)+";"
                       + str(pais.nodo_valor.borders_airports)+";"
                       +str(pais.nodo_valor.infeccion)+";"+
                       str(pais.nodo_valor.cura)+ ";"+str(pais.nodo_valor.progreso_cura)+ "\n")
        file.close()
        file2 = open("pandemia_"+str(nombre)+".csv", "w")
        file2.write("Nombre,dias_pasados,tipo"+"\n")
        file2.write(str(pandemia.name)+","+str(pandemia.dias)+","+str(pandemia.tipo))
        file2.close()


if __name__ == "__main__":
    pass