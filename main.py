from PyQt5 import QtGui, QtWidgets
import sys
import gui
from cartesiangraph import customgen

class PassGenApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
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

        self.spinBox.setValue(len(in_password))
        self.textEdit.append(" --- Generating --- ")
        customgen(in_password, file_name, self.textEdit)
        self.textEdit.append(" --- Generated --- ")
        self.textEdit.append(" ------ Changes were written to %s ------- " % file_name)
        self.textEdit.append(" ... ")
        self.textEdit.append(" / ")

    def refreshTextArea(self, password):
        self.textEdit.append(password)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = PassGenApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()