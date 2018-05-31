import ConsultasBasicas


def leer_consulta(array):
    global i
    lista = [ConsultasBasicas.lector(x) for x in array]
    text2 = [("----- Consulta {} -----\n".format(next(i)))+str(x)+"\n" for x in lista]
    text2 = "".join(text2)

    return text2


def contador():
    h = 1
    while True:
        yield i
        h += 1

i = contador()


def generar_archivo(array):
    j = contador()
    lista = [ConsultasBasicas.lector(x) for x in array]
    texto = [("----- Consulta {} -----\n".format(next(j))) +
             str(x) + "\n" for x in lista]
    texto = "".join(texto)
    archivo = open("resultados.txt", "w")
    archivo.write(texto)
    archivo.close()

if __name__ == "__main__":
    pass
