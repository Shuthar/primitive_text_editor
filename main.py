from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,  QMenuBar, QMenu, QFileDialog

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(250, 300, 350, 200)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.action_cliced)
        fileMenu.addAction("Сохранить", self.action_cliced)

    @QtCore.pyqtSlot()
    def action_cliced(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print("no such file")

        if action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("no such file")

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()