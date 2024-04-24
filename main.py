from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

day = 1


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 100, 100)
    win.setWindowTitle("Hei")

    win.show()
    sys.exit(app.exec_())


window()
