import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QLinearGradient, QBrush
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt_design.ui',self)
        #self.dolar.clicked.connect(self.dollars)

    def dollars(self):
        pass
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())