from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys
import Varios


class T03Window(MyWindow):
    def __init__(self):
        self.i = 1
        super().__init__()

    def process_consult(self, querry_array):
        # Agrega en pantalla la solución. Muestra los graficos!!

        text2 = str(Varios.leer_consulta(querry_array))
        self.i += 1
        self.add_answer(str(text2)+"\n")

    def save_file(self, querry_array):
        # Crea un archivo con la solucion. NO muestra los graficos!!
        Varios.generar_archivo(querry_array)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
