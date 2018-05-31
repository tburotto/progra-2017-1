from Lectort import *
import random
from Gobierno import *


class Cura:
    def __init__(self, pandemia):
        self.cura = 0
        self.infectados = pandemia.infectados
        self.dias = pandemia.dias
        self.populacion_total = pandemia.populacion
        self.muertos = pandemia.muertos
        self.visibilidad = pandemia.visibilidad

    def descubrir_infeccion(self,pandemia):
        probabilidad = min((10**7)*(self.visibilidad * self.infectados * (self.muertos**2))/(self.populacion_total**3),1)
        rand = random.random()
        if rand <= probabilidad:
            return True
        else:
            return False

class Pandemic:
    def __init__(self, tipo, nombre, pais_inicial):
        print("")
        print(" CARGANDO JUEGO...")
        self.cura = 0
        self.resumen = ""
        self.name = nombre
        self.tipo = tipo
        if self.tipo == "Bacteria":
            self.contagiosidad = 1
            self.mortalidad = 1
            self.resistencia = 0.5
            self.visibilidad = 0.7
        elif self.tipo == "Virus":
            self.contagiosidad = 1.5
            self.mortalidad = 1.2
            self.resistencia = 1.5
            self.visibilidad = 0.5
        elif self.tipo == "Parasito":
            self.contagiosidad = 0.5
            self.mortalidad = 1.5
            self.resistencia = 1
            self.visibilidad = 0.45
        else:
            raise Warning
        self.paises_infectados = ListaLigada()
        self.populacion = 0
        self.dias = 0
        self.paises = ListaLigada()
        self.muertos = 0
        self.infectados = 0
        self.population_lista = Lector().abrir_population()
        for i in self.population_lista:
            if i[0].nodo_valor == "Pais":
                continue
            else:
                pais = Pais(i[0].nodo_valor)
                self.paises.append(pais)
                self.populacion += int(i[1].nodo_valor)
        self.population_lista = None
        self.pais_inicial = pais_inicial
        for pais in self.paises:
            if pais.nodo_valor.nombre == self.pais_inicial and pais.nodo_valor.infectados == 0:
                pais.nodo_valor.agregar_infectado()
                self.paises_infectados.append(pais.nodo_valor)
        for pais in self.paises:
            self.infectados += pais.nodo_valor.infectados
            self.muertos += pais.nodo_valor.muertos

    def start(self):
        while True:
            print("")
            print("Estas son tus posibilidades:")
            print("1) Obtener estadisticas actualizadas")
            print("2) Pasar de dia")
            print("3) Guardar estado de juego")
            print("4) Salir")
            desicion = str(input("Que deseas hacer: "))
            if desicion == "1":
                print("")
                print("Estas son las estadisticas disponibles:")
                print("")
                print("1) Estado por pais")
                print("2) Estado mundial")
                print("3) Estado de las tasas de infeccion o muerte por dia")
                print("4) Resumen de sucesos del dia")
                print("5) Volver")
                print("")
                desicion2 = str(input("Eleccion: "))
                if desicion2 == "1":
                    Estadisticas(self).estadisticasporpais()
                elif desicion2 == "2":
                    Estadisticas(self).estadisticas_mundiales()
                elif desicion2 == "3":
                    pass
                elif desicion2 == "4":
                    Estadisticas(self).resumen()
                elif desicion2 == "5":
                    self.start()
                else:
                    print("Hubo un error en la seleccion")
                    self.start()

            elif desicion == "2":
                print("")
                print("Ha pasado un dia!")
                self.pasar_dia()

            elif desicion == "3":
                print("")
                print("Guardando juego...")
                Lector().guardar_juego(self)
                print("Juego guardado como: "+str(self.name)+".")

            elif desicion == "4":
                break
            else:
                print ("Hubo un error en la seleccion")
                self.start()

    def pasar_dia(self):
        self.resumen = ""
        self.dias += 1
        self.infectados = 0
        self.muertos = 0
        self.infectados_viejos = self.infectados
        self.muertos_viejos = self.muertos
        for pais in self.paises:
            pais.nodo_valor.pasar_dia(self)
            self.infectados += pais.nodo_valor.infectados
            self.muertos += pais.nodo_valor.muertos
        self.muertos_dia = self.muertos - self.muertos_viejos
        self.infectados_dia = self.infectados - self.infectados_viejos
        if Cura(self).descubrir_infeccion(self) and self.cura == 0:
            self.cura = 1
            for pais in self.paises:
                if random.randint(0,1) == 1 and pais.nodo_valor.infectados > 0:
                    print("Se ha descubierto la enfermedad "+str(self.name)+" en "+str(pais)+"!")
                    print(str(pais)+" comenzara a trabajar inmediatamente en la cura!")
                    pais.nodo_valor.infeccion = True
                    self.resumen = self.resumen + "Se ha descubierto la enfermedad "+str(self.name)+" en "+str(pais)+"!\n"
                    break
        if self.muertos == self.populacion:
            print("")
            print("Has ganado, todos estan muertos!")
            exit()
        if self.infectados == 0 and self.muertos != self.populacion:
            print("Lo siento, la humanidad se ha salvado")
            exit()

    def infectar_pais_tierra(self, pais):
        for i in self.paises:
            if i.nodo_valor.infectados == 0 and str(i.nodo_valor.nombre) == pais and i.nodo_valor.fronteras:
                i.nodo_valor.agregar_infectado()
                self.paises_infectados.append(i.nodo_valor)
                print("Pais " + str(i.nodo_valor) + " infectado!")
                self.resumen = self.resumen + "- Pais " + str(i.nodo_valor) + " infectado por tierra!\n"

    def infectar_pais_aire(self, pais):
        for i in self.paises:
            if i.nodo_valor.infectados == 0 and str(i.nodo_valor.nombre) == pais and i.nodo_valor.aeropuerto:
                i.nodo_valor.agregar_infectado()
                self.paises_infectados.append(i.nodo_valor)
                print("Pais " + str(i.nodo_valor) + " infectado!")
                self.resumen = self.resumen + "- Pais " + str(i.nodo_valor) + " infectado por avion!\n"



class Pais:
    def __init__(self, nombre):
        self.cura = False
        self.estado = "LIMPIO"
        self.fronteras = True
        self.infectados_totales = 0
        self.progreso_cura = 0
        self.populacion_mundial = 0
        self.dia_actual = 0
        self.dias_descubrimiento = 0
        self.infeccion = False
        self.mascarillas = False
        self.dias_infectado = 0
        self.nombre = nombre
        self.muertos = 0
        self.infectados = 0
        self.lista_populacion = Lector().abrir_population()
        for i in self.lista_populacion:
            if i[0].nodo_valor == self.nombre:
                self.populacion = int(i[1].nodo_valor)
                break
        self.lista_populacion = None
        self.lista_airports = Lector().abrir_airports()
        if self.lista_airports.isin(self.nombre):
            self.aeropuerto = True
        else:
            self.aeropuerto = False
        self.lista_airports = None
        self.saludables = self.populacion - self.infectados - self.muertos
        self.vivos = self.populacion

        self.dic_borders = Lector().abrir_borders()
        if not self.dic_borders.isin(self.nombre):
            self.dic_borders.append(Key(self.nombre, ListaLigada()))

        for elemento in self.dic_borders.lista:
            if elemento.nodo_valor.value.isin(self.nombre):
                if not self.dic_borders[self.nombre].isin(elemento.nodo_valor.key):
                    self.dic_borders[self.nombre].append(elemento.nodo_valor.key)

        self.dic_borders_airports = Lector().random_airports()
        if not self.dic_borders_airports.isin(self.nombre):
            self.dic_borders_airports.append(Key(self.nombre, ListaLigada()))

        for elemento in self.dic_borders_airports.lista:
            if elemento.nodo_valor.value.isin(self.nombre):
                if not self.dic_borders_airports[self.nombre].isin(elemento.nodo_valor.key):
                    self.dic_borders_airports[self.nombre].append(elemento.nodo_valor.key)

        self.borders = self.dic_borders[self.nombre]
        self.borders_airports = self.dic_borders_airports[self.nombre]

    def agregar_infectado(self):
        self.infectados += 1
        self.saludables -= 1
        self.estado = "INFECTADO"

    def pasar_dia(self, pandemia):
        self.populacion_mundial = pandemia.populacion
        self.dia_actual += 1
        gobierno = Gobierno(self)
        gobierno.calcular_cola(pandemia)
        gobierno.ordenar_cola()
        gobierno.ejecutar_ordenes(pandemia)
        self.avanzar_cura()
        if self.infectados >= 1:
            self.afectarpais(pandemia)
            self.infectar_vecinos(pandemia)
            self.dias_infectado += 1
        else:
            pass

    def infectar_vecinos(self, pandemia):
        if (self.infectados / self.populacion) >= 0.2 and self.fronteras:
            try:
                probabilidad_de_infeccion = min((7*self.infectados_totales) / ((self.vivos)*
                                                                          (len(self.borders)+len(self.borders_airports))), 1)
            except ZeroDivisionError:
                probabilidad_de_infeccion = 0
            for elemento in self.borders:
                p = random.random()
                if probabilidad_de_infeccion > p:
                    pandemia.infectar_pais_tierra(elemento.nodo_valor)

        if (pandemia.infectados / pandemia.populacion) >= 0.04 and self.aeropuerto:
            try:
                probabilidad_de_infeccion = min((7 * self.infectados_totales) /
                                                (self.vivos * (len(self.borders)+len(self.borders_airports))), 1)


            except ZeroDivisionError:
                probabilidad_de_infeccion = 0

            for p in self.borders_airports:
                rand = random.random()
                if probabilidad_de_infeccion >= rand:
                    for pais in pandemia.paises:
                        if pais.nodo_valor.nombre == p.nodo_valor:
                            if pais.nodo_valor.aeropuerto:
                                pandemia.infectar_pais_aire(p.nodo_valor)

    def __repr__(self):
        return self.nombre

    def afectarpais(self, pandemia):
        if self.cura:
            desinfectados = int(0.25*self.infectados*pandemia.resistencia)
            self.infectados -= desinfectados

        muertos = 0
        nuevas_infecciones = 0

        if self.infectados == 0:
            return
        else:
            if self.saludables > 0:
                nuevas_infecciones = int(int(random.randint(0, 6)*pandemia.contagiosidad)*self.infectados*0.5)
            if self.mascarillas:
                nuevas_infecciones = int(nuevas_infecciones * 0.3)
            if self.saludables - nuevas_infecciones < 0:
                nuevas_infecciones = self.saludables
        if self.vivos < 10000000:
            probabilidad_de_muerte = min(min(0.2, (int(self.dias_infectado) ** 2)/1000000)*pandemia.mortalidad,1)
        else:
            probabilidad_de_muerte = min(min(0.2, (int(self.dias_infectado) ** 2)/1000000)*pandemia.mortalidad,1)
        if self.vivos > 0:
            muertos = int(self.infectados * probabilidad_de_muerte)
        if self.vivos - muertos < 0:
            muertos = self.vivos

        if self.vivos < 10000:
            muertos = int(self.vivos/3)
            if self.vivos < 100:
                muertos = int(self.vivos)

        self.muertos += muertos
        self.infectados += nuevas_infecciones
        self.saludables -= nuevas_infecciones
        self.vivos -= muertos
        self.infectados -= muertos
        self.infectados_totales += nuevas_infecciones
        if self.infectados > 0:
            self.estado = "INFECTADO"
        elif self.vivos == 0:
            self.estado = "MUERTO"
        elif self.saludables == self.populacion:
            self.estado = "LIMPIO"

    def avanzar_cura(self):
        if self.progreso_cura >= 100:
            return
        if self.infeccion == False:
            return
        else:
            self.dias_descubrimiento += 1
            self.progreso_cura += self.saludables*100/(2*self.populacion_mundial)
        if self.progreso_cura >= 100:
            self.cura = True



class Estadisticas:
    def __init__(self, pandemia):
        self.pandemia = pandemia
        self.paises = pandemia.paises

    def estadisticasporpais(self):
        print("")
        npais = str(input("Que pais quieres observar: "))
        for pais in self.paises:
            if npais == pais.nodo_valor.nombre:
                print("")
                print("Estas son las estadisticas")
                print("Poblacion inicial : " + str(pais.nodo_valor.populacion))
                print("Cantidad de infectados: " + str(pais.nodo_valor.infectados))
                print("Cantidad de muertos: " + str(pais.nodo_valor.muertos))
                print("Dias infectado: " + str(pais.nodo_valor.dias_infectado))
                print("Avance de la cura: "+ str(pais.nodo_valor.progreso_cura)+"%")
                print("Personas Saludables: "+ str(pais.nodo_valor.saludables))
                print("Personas Vivas: " + str(pais.nodo_valor.vivos))

    def estadisticas_mundiales(self):
        print("")
        print("")
        print("Estas son las estadisticas")
        print("Poblacion inicial : " + str(self.pandemia.populacion))
        print("Cantidad de infectados: " + str(self.pandemia.infectados))
        print("Cantidad de muertos: " + str(self.pandemia.muertos))
        print("Dias infectado: " + str(self.pandemia.dias))
        print("Paises Infectados: ")
        infectados = ListaLigada()
        muertos = ListaLigada()
        limpios = ListaLigada()
        for pais in self.pandemia.paises:
            if pais.nodo_valor.estado == "LIMPIO":
                limpios.append(pais.nodo_valor.nombre)
            elif pais.nodo_valor.estado == "MUERTO":
                muertos.append(pais.nodo_valor.nombre)
            elif pais.nodo_valor.estado == "INFECTADO":
                infectados.append(pais.nodo_valor.nombre)
        print(infectados)
        print("Paises Muertos")
        print(muertos)
        print("Paises Limpios: ")
        print(limpios)

    def resumen(self):
        print("")
        print("- Hoydia murieron "+str(self.pandemia.muertos_dia)+" personas.")
        print("- Hoydia se infectaron "+str(self.pandemia.infectados_dia)+" personas")
        print("Los sucesos son:")
        print("")
        print(self.pandemia.resumen)


if __name__ == "__main__":
    chile = Pais("Uruguay")
    print(chile.borders_airports)