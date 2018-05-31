from Estructuras import *

class Gobierno:
    def __init__(self, pais):
        self.pais = pais
        self.dias_infectado = pais.dias_infectado
        self.infectados = pais.infectados
        self.populacion = pais.populacion
        self.cola_prioridades = ListaLigada()
        self.cola_prioridades_final = ListaLigada()


    def calcular_cola(self, pandemia):
        self.cola_prioridades = ListaLigada()
        suma = 0
        i = 0
        # Mascarillas, se reparten mascarillas si 1/3 de la populacoion del pais esta infectado
        if self.infectados / self.populacion >= (1/3):
            mascarillas = ListaLigada("Mascarillas", (0.5*self.infectados)/self.populacion)
            self.cola_prioridades.append(mascarillas)

        if self.infectados / self.pais.vivos >= 1/2 or self.pais.muertos / self.populacion >= 1/4:
            i = 0
            for pais in pandemia.paises:
                if pais.nodo_valor.borders.isin(self.pais.nombre):
                    suma += (pais.nodo_valor.infectados / pais.nodo_valor.vivos)
                    i += 1
            if i == 0:
                promedio = 0
            else:
                promedio = suma / i
            cerrar_fronteras = ListaLigada("Cerrar Fronteras", (promedio*self.infectados)/self.populacion)
            self.cola_prioridades.append(cerrar_fronteras)

        if self.infectados / self.pais.vivos >= 0.8 or self.pais.muertos/self.populacion >= 0.2 and self.pais.aeropuerto:
            cerrar_aeropuerto = ListaLigada("Cerrar Aeropuerto", (0.8*self.infectados)/self.populacion)
            self.cola_prioridades.append(cerrar_aeropuerto)

        if (self.infectados / self.pais.vivos < 0.8 or self.pais.muertos/self.populacion < 0.2) and not self.pais.aeropuerto \
                and len(self.pais.borders_airports) > 0:
            abrir_aeropuerto = ListaLigada("Abrir Aeropuerto", (0.8 * self.infectados) / self.populacion)
            self.cola_prioridades.append(abrir_aeropuerto)

        if (self.infectados / self.pais.vivos < 1 / 2 or self.pais.muertos / self.populacion < 1 / 4) and not self.pais.fronteras:
            i = 0
            for pais in pandemia.paises:
                if pais.nodo_valor.borders.isin(self.pais.nombre):
                    suma += (pais.nodo_valor.infectados / pais.nodo_valor.vivos)
                    i += 1
            if i == 0:
                promedio = 0
            else:
                promedio = suma / i
            abrir_fronteras = ListaLigada("Abrir Fronteras", (promedio * self.infectados) / self.populacion)
            self.cola_prioridades.append(abrir_fronteras)



    def ordenar_cola(self):
        cola = ListaLigada()
        while len(cola)!=len(self.cola_prioridades):
            prioridad_maxima = 0
            elemento_prioritario = None
            for elemento in self.cola_prioridades:
                if elemento_prioritario == None and not cola.isin(elemento.nodo_valor[0].nodo_valor):
                    elemento_prioritario = elemento.nodo_valor[0].nodo_valor
                    prioridad_maxima = elemento.nodo_valor[1].nodo_valor
                else:
                    if elemento.nodo_valor[1].nodo_valor > prioridad_maxima \
                            and not cola.isin(elemento.nodo_valor[0].nodo_valor):
                        elemento_prioritario = elemento.nodo_valor[0].nodo_valor
                        prioridad_maxima = elemento.nodo_valor[1].nodo_valor

            cola.append(elemento_prioritario)

        self.cola_prioridades_final = cola

    def ejecutar_ordenes(self,pandemia):
        i = 0
        for pais in pandemia.paises:
            if pais.nodo_valor.nombre == self.pais.nombre:
                for elemento in self.cola_prioridades_final:
                    if i == 3:
                        break
                    else:
                        if elemento.nodo_valor == "Cerrar Aeropuerto" and pais.nodo_valor.aeropuerto:
                            pais.nodo_valor.aeropuerto = False
                            pandemia.resumen = pandemia.resumen + "- "+\
                                               str(self.pais.nombre)+ " ha cerrado su aeropuerto\n"

                        elif elemento.nodo_valor == "Cerrar Fronteras" and pais.nodo_valor.fronteras:
                            pais.nodo_valor.fronteras = False
                            pandemia.resumen = pandemia.resumen + "- " + str(
                                self.pais.nombre) + " ha cerrado sus fronteras\n"

                        elif elemento.nodo_valor == "Mascarillas" and not pais.nodo_valor.mascarillas:
                            pais.nodo_valor.mascarillas = True
                            pandemia.resumen = pandemia.resumen + "- " + str(
                                self.pais.nombre) + " ha repartido mascarillas\n"

                        elif elemento.nodo_valor == "Abrir Aeropuerto" and not pais.nodo_valor.aeropuerto:
                            pais.nodo_valor.aeropuerto = True
                            pandemia.resumen = pandemia.resumen + "- " + str(
                                self.pais.nombre) + " ha abierto su aeropuerto\n"

                        elif elemento.nodo_valor == "Abrir Fronteras" and not pais.nodo_valor.fronteras:
                            pais.nodo_valor.fronteras = True
                            pandemia.resumen = pandemia.resumen + "- " + str(
                                self.pais.nombre) + " ha abierto sus fronteras\n"


                    i += 1







