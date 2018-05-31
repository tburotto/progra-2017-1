from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys

fond = uic.loadUiType("T05window/main.ui")

class MainWindow(fond[0], fond[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    fond = MainWindow()
    fond.show()
    sys.exit(app.exec())