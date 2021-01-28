from PyQt5.QtWidgets import *
from mainwindow import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_2.triggered.connect(self.openFileDialog)
        self.ui.actionSave.triggered.connect(self.saveFileDialog)
        self.show()

    def openFileDialog(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fileName[0]:
            file = open(fileName[0], 'r')
            with file:
                data = file.read()
                self.ui.textEdit.setText(data)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_Name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);; Text "
                                                                                              "Files (*.txt)",
                                                   options=options)
        fileName = open(file_Name, 'w')
        text = self.ui.textEdit.toPlainText()
        fileName.write(text)
        fileName.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())
