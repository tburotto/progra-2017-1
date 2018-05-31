class Excepcion2(Exception):
    def __init__(self, descifrador):
        # Esta clase retorna un codigo nuevo, es decir realiza limpiador
        # nuevamente pero inivierte los chunks despues de a
        super().__init__()
        self.descifrador = descifrador
        self.descifrador.lectura_archivo()
        lista = self.descifrador.codigo.split(" ")
        codigo = ''
        c = 1
        for elemento in lista:
            if c == 0:
                k = elemento[::-1]
                if len(k) < 6 or len(k) > 7:
                    pass
                else:
                    codigo += ' ' + k
            elif "a" in elemento:
                k = ""
                for i in elemento:
                    if i == "a":
                        continue
                    else:
                        k += i
                k = k[::-1]
                c = 0
                if len(k) < 6 or len(k) > 7:
                    pass
                else:
                    codigo += ' ' + k
            else:
                k = elemento
                if len(k) < 6 or len(k) > 7:
                    pass
                else:
                    codigo += ' ' + k
        self.codigo = codigo


class Descifrador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suma=0
        with open(self.nombre, "r") as self.archivo:
            lineas = self.archivo.readlines()
            self.codigo = ''
            self.texto = "".join(lineas).replace('\n', '')
            i = 0

    def lectura_archivo(self):
        with open(self.nombre, "r") as archivo:
            lineas = archivo.readlines()
            self.codigo = ''
            texto = "".join(lineas).replace('\n', '')
            for caracter in texto:
                self.codigo += caracter
            return self.codigo

    def elimina_incorrectos(self):
        try:
            lista=self.codigo.split(" ")
            self.codigo=''
            for i in lista:
                if "a" in i:
                    raise Excepcion2(self)
                if len(i) < 6 or len(i) > 7:
                    pass
                else:
                    self.codigo += ' '+i

        except Excepcion2 as err:
            self.codigo = err.codigo # Esto fue lo que se me ocurrio (y funciona) pero nose si es valido :D
                                    # Revisar la Class Excepcion2 para eneteder como funciona


        finally:
            return self.codigo

    def cambiar_binario(self, binario):
        try:
            lista = binario.split(' ')
            texto = []
            for x in lista[1:]:
                texto.append(chr(int(x, 2)))
        except IndexError:
            pass

        finally:
            return texto

    def limpiador(self, lista):
        try:
            i = -1
            string = ''

            while i < len(lista):
                i += 1
                if '$' != lista[i]:
                    string += lista[i]
        except Exception as err:
            print(err)

        finally:
            return string

if __name__ == "__main__":

    try:
        des = Descifrador('mensaje_marciano.txt')
        codigo= des.lectura_archivo()
        codigo=des.elimina_incorrectos()
        lista = des.cambiar_binario(des.codigo)
        texto = des.limpiador(lista)
        print(texto)

    except Exception as err:
        print('Esto no debiese imprimirse')

