'''
Thiết kế như hình a:
Yêu cầu: Người dùng click vào Change Font sẽ hiển thị ra bảng màu như hình b,font được
chọn sẽ hiệu ứng lên text bạn gõ trong textbox như hình c
'''

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFontDialog,QApplication,QDialog
from change import *

class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changeFont)
        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok :
            self.ui.textEdit.setFont(font)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())