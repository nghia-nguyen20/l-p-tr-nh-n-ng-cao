'''
Thiết kế như hình a:
Yêu cầu: Người dùng click vào Choose color sẽ hiển thị ra bảng màu như hình b,
màu được chọn sẽ hiển thị lên Label tương ứng như hình c
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from color import *


class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        color = QColor(0, 0, 0)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.frame.setStyleSheet("QWidget {background-color: %s}" % color.name())
        self.ui.pushButton.clicked.connect(self.disColor)
        self.show()

    def disColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.frame.setStyleSheet("QWidget { background-color: %s}" % color.name())
            self.ui.label.setText(" you have selected the color with code: " + str(color.name()))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())
