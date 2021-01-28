''' NGUYEN THI NGHIA - 3001190529 - CD19LW9'''

'''Thiết kế như hình a:
Yêu Cầu: Người dùng click vào Choose Country sẽ hiển thị ra Input Dialog chứa những
Country như hình b, sau đó thông tin hiển thị lên lại textbox Your Country như hình c
'''

from PyQt5.QtWidgets import *
from click import *
class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changeCountry)

    def changeCountry(self):
        countries = (
            "Albania",
            "Argentina",
            "Andorra"
        )
        countryName, ok = QInputDialog.getItem(self, "Input Dialog", "List of countries", countries, 0, False)
        if ok and countryName:
            self.ui.lineEdit.setText(countryName)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())

