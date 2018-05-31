
from Plague import *

def cargar_juego(nombre):
    try:
        file1 = open("paises_" + str(nombre) + ".csv", "r")
        file2 = open("pandemia_" + str(nombre) + ".csv", "r")
        for lines in file2:
            linea = lines.strip("\n")
            linea = split(linea, ",")
            if linea[0].nodo_valor == "Nombre":
                continue
            else:
                pandemia = Pandemic(linea[2].nodo_valor, linea[0].nodo_valor, "")
                pandemia.dias = int(linea[1].nodo_valor)
        paises = ListaLigada()
        for lines in file1:
            linea = lines.strip("\n")
            linea = split(linea, ";")
            if linea[0].nodo_valor == "Nombre":
                continue
            else:
                pais = Pais(linea[0].nodo_valor)
                pais.dias_infectado = int(linea[1].nodo_valor)
                pais.infectados = int(linea[2].nodo_valor)
                pais.muertos = int(linea[3].nodo_valor)
                pais.aeropuerto = str(linea[4].nodo_valor)
                if pais.aeropuerto == "True":
                    pais.aeropuerto = True
                else:
                    pais.aeropuerto = False
                lista_borders_airports = string_a_lista(linea[6].nodo_valor)
                pais.borders_airports = lista_borders_airports
                pais.infeccion = str(linea[7].nodo_valor)
                if pais.infeccion == "True":
                    pais.infeccion = True
                else:
                    pais.infeccion = False
                if pais.infeccion:
                    pandemia.cura = 1
                pais.cura = str(linea[8].nodo_valor)
                if pais.cura == "True":
                    pais.cura = True
                else:
                    pais.cura = False
                pais.progreso_cura = float(linea[9].nodo_valor)
                paises.append(pais)


        pandemia.paises = paises
        return pandemia

    except FileNotFoundError:
        print("No se encontro el archivo!")
        return

if __name__ == "__main__":
    print(2**2)