import SuperLuchin
import Metereologia
import lector


class Inicializar_Clima:
    def __init__(self, fecha, hora):
        self.fecha_actual = fecha
        self.hora_actual = hora
        self.Hora_Fecha = SuperLuchin.Hora_Fecha(self.fecha_actual, self.hora_actual)
        self.lista_clima = lector.abrir("meteorologia.csv")
        self.incendios_activos = []
        self.all_clima = []
        lista = lector.abrir("incendios.csv")
        lista.pop(0)
        for k in lista:
            if k[0] == "id:string":
                continue
            incendio = SuperLuchin.Incendio(k[0], self.Hora_Fecha)
            if self.Hora_Fecha >= incendio.fecha:
                self.incendios_activos.append(incendio)
        i = 0
        for k in self.incendios_activos:
            if k.puntos_poder <= 0:
                self.incendios_activos.pop(i)
            i += 1
        for k in self.lista_clima:
            if k[0] == "id:string:":
                continue
            self.all_clima.append(Metereologia.Clima(k[0]))

    def afectar_incendios(self):
        for clima in self.all_clima:
            for incendio in self.incendios_activos:
                if clima.fecha_inicio >= incendio.fecha:
                    if incendio.fecha >= clima.fecha_inicio and clima.fecha_termino >= self.Hora_Fecha:
                        horas = self.Hora_Fecha - incendio.fecha
                    elif incendio.fecha >= clima.fecha_inicio and self.Hora_Fecha >= clima.fecha_termino:
                        horas = clima.fecha_termino - incendio.fecha
                    elif clima.fecha_inicio >= incendio.fecha and clima.fecha_termino >= self.Hora_Fecha:
                        horas = clima.fecha_termino - incendio.fecha
                    elif clima.fecha_inicio >= incendio.fecha and self.Hora_Fecha >= clima.fecha_termino:
                        horas = clima.fecha_termino - clima.fecha_inicio

                    if (clima.lat_min < incendio.lat_max < clima.lat_max) or \
                            (clima.lat_min < incendio.lat_min < clima.lat_max) or \
                            ((incendio.lat_min < clima.lat_min < incendio.lat_max) and (incendio.lat_min < clima.lat_max < incendio.lat_max )):
                        if (clima.lon_min < incendio.lon_max < clima.lon_max) or (
                                clima.lon_min < incendio.lon_min < clima.lon_max) or (
                            (incendio.lon_min < clima.lon_min < incendio.lon_max) and (
                                incendio.lon_min < clima.lon_max < incendio.lon_max)):
                            if clima.tipo == "VIENTO":
                                incendio.check_viento(clima, horas)
                            elif clima.tipo == "LLUVIA":
                                incendio.check_lluvia(clima, horas)
                            elif clima.tipo == "TEMPERATURA":
                                incendio.check_temperatura(clima, horas)

        return self.incendios_activos



