from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import sys
import gui
from cartesiangraph import customgen

class PassGenThread(QThread):

    password = ""
    filename = ""
    displaywidget = None

    def __init__(self, _p, _f, _d):
        QThread.__init__(self)
        self.password = _p
        self.filename = _f
        self.displaywidget = _d

    def __del__(self):
        self.wait()

    def run(self):
        customgen(self.password, self.filename, self.displaywidget)
        return

class PassGenApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    pysign = pyqtSignal(str)

    def __init__(self, parent=None):
        super(PassGenApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browseFolder)
        self.pushButton_2.clicked.connect(self.generatePassword)


    def browseFolder(self):
        self.lineEdit_2.clear()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           "Pick a file")
        if file_name:
            self.lineEdit_2.setText(file_name)


    def generatePassword(self):
        file_name = self.lineEdit_2.text()
        if not file_name:
            file_name = "temp.txt"

        in_password = self.lineEdit.text()
        if not in_password:
            return

        self.spinBox.setValue(self.countLength(in_password))
        self.textEdit.append(" --- Generating --- ")

        self.pysign.connect(self.refreshTextArea)

        self.passgenthread = PassGenThread(in_password, file_name, self.pysign)
        self.passgenthread.start()

        self.textEdit.append(" --- Multi Threading --- ")
        self.textEdit.append(" ------ Changes are being written to %s ------- " % file_name)
        self.textEdit.append(" ... ")
        self.textEdit.append(" / ")

    def refreshTextArea(self, password):
        self.textEdit.append(password)

    def countLength(self, input_str):
        counter = 0
        bool_unknown = False
        for c in input_str:
            if c == "(":
                bool_unknown = True
            elif c == ")":
                bool_unknown = False
            if not bool_unknown:
                counter += 1
        return counter

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = PassGenApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
