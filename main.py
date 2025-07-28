from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtWidgets
import sys

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setGeometry(700, 300, 450, 550)  # nustatomas lango dydis
        self.setWindowTitle("Calculator")

        self.setupUI()

    def setupUI(self):
        self.text = QLabel(self)
        self.text.setText("This is text")
        self.text.move(50, 50)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('Click me')
        self.btn1.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.text.setText("This text has been changed")

def main():
    app = QApplication(sys.argv)
    win = Ui_MainWindow() #sukuriamas langas

    win.show() #atidarome langa
    sys.exit(app.exec())#uzdarome langa baige

main()
