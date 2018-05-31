
class Nodo:
    def __init__(self, valor):
        self.nodo_valor = valor
        self.siguiente = None

    def __repr__(self):
        return str(self.nodo_valor)

    def __getitem__(self, item):
        return self.nodo_valor[item]


class ListaLigada:
    def __init__(self, *args):
        self.cabeza = None
        self.cola = None
        self.siguiente = None
        for arg in args:
            if not self.cabeza:
                self.cabeza = Nodo(arg)
                self.cola = self.cabeza
            else:
                self.cola.siguiente = Nodo(arg)
                self.cola = self.cola.siguiente

    def append(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente

    def __repr__(self):
        s = "["  + str(self.cabeza)
        if not self.cabeza:
            return "[]"
        self.siguiente = self.cabeza.siguiente
        while self.siguiente:
            s += ", " + str(self.siguiente)
            self.siguiente = self.siguiente.siguiente

        s += "]"
        return s

    def sort(self):
        lista_nueva = ListaLigada()
        prioridad = None
        for elemento in self:
            if not prioridad:
                elemento = prioridad
            if elemento.nodo_valor >= prioridad:
                lista_nueva.append(elemento)
            else:
                continue
        return lista_nueva


    def __getitem__(self, item):
        nodo = self.cabeza
        for i in range(item):
            if nodo:
                nodo = nodo.siguiente
            else:
                raise IndexError
        if not nodo:
            raise IndexError
        return nodo

    def __setitem__(self,i, valor):
        for elemento in self:
            if self[i].nodo_valor == elemento.nodo_valor:
                elemento.nodo_valor = valor
            else:
                continue

    def __len__(self):
        i = 0
        for _ in self:
            i += 1
        return i

    def isin(self, valor):
        nodo = self.cabeza
        while nodo:
            if nodo.nodo_valor == valor:
                return True
            else:
                nodo = nodo.siguiente
                if not nodo:
                    return False

    def search(self, item):
        nodo = self.cabeza
        while nodo:
            if nodo.nodo_valor == item:
                return nodo.nodo_valor
            else:
                nodo = nodo.siguiente
                if not nodo:
                    return False


def split(string, spliter):
    if not isinstance(spliter, str) or not isinstance(string, str):
        raise Exception("No es un string!")
    lista_ligada = ListaLigada()
    a = ""
    for letra in string:
        if not letra == spliter:
            a += letra
        else:
            lista_ligada.append(a)
            a = ""
    lista_ligada.append(a)
    return lista_ligada

def string_a_lista(string):
    try:
        lista_en_str = string.replace("[","")
        lista_en_str = lista_en_str.replace("]","")
        lista_ligada = split(lista_en_str, ",")
        for elemento in lista_ligada:
            if elemento.nodo_valor[0] == " ":
                elemento.nodo_valor = elemento.nodo_valor[1:]
        return lista_ligada

    except IndexError:
        return ListaLigada()





class Key:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.listak = ListaLigada(key, value)

    def __repr__(self):
        return str(self.key) +": " + str(self.value)


class Dict:
    def __init__(self, *args):
        self.lista = ListaLigada()
        for arg in args:
            self.lista.append(arg)

    def append(self, key):
        self.lista.append(key)

    def __repr__(self):
        s = "{"
        for key in self.lista:
            s += str(key) + ", "
        s = s.rstrip(", ")
        s += "}"
        return s

    def isin(self, item):
        for elemento in self.lista:
            if elemento.nodo_valor.listak[0].nodo_valor == item:
                return True
        return False

    def __getitem__(self, item):
        for i in self.lista:
            if i.nodo_valor.listak[0].nodo_valor == item:
                return i.nodo_valor.listak[1].nodo_valor

        return False

    def erase(self, item):
        lista = ListaLigada()
        for key in self.lista:
            if key.nodo_valor.listak[0].nodo_valor == item:
                continue
            else:
                lista.append(key.nodo_valor)
        self.lista = lista

    def __setitem__(self, key, value):
        for keys in self.lista:
            if keys.nodo_valor.listak[0].nodo_valor == key:
                self.erase(key)
                self.append(Key(key, value))
                return

if __name__ == "__main__":
    lista = ListaLigada(4,5,21,1)
    lista = lista.sort()
    print(lista)



