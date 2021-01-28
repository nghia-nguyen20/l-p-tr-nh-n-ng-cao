from PyQt5.QtWidgets import *
from Tienluong import *
from PyQt5.QtGui import QCursor


class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class Test(MyApp):
    def __init__(self):
        super(Test, self).__init__()
        self.ui.pushButton.clicked.connect(self.TinhLuong)
        self.ui.pushButton_2.clicked.connect(self.TiepTuc)
        self.ui.pushButton_3.clicked.connect(self.Thoat)

    def TinhLuong(self):
        maso = self.ui.lineEdit_2.text()
        hoten = self.ui.lineEdit.text()
        mucluong = self.ui.lineEdit_3.text()
        ngaycong = self.ui.lineEdit_4.text()
        doanhso = int(self.ui.lineEdit_5.text())
        hoahong = 0
        luong = (int(mucluong) / 24) * int(ngaycong)
        luongthang = 0
        if doanhso <= 5000000:
            hoahong = 0
        elif doanhso > 5000000 and doanhso <= 10000000:
            hoahong = luong * 0.05
        elif doanhso > 10000000 and doanhso <= 15000000:
            hoahong = luong * 0.1
        else:
            hoahong = luong * 0.15
        luongthang = luong + hoahong
        ketqua = ''
        ketqua += 'Tên Nhân Viên: ' + str(hoten)
        ketqua += '\n' + 'Lương Tháng: ' + str(luong) + ' Đồng'
        ketqua += '\n' + 'Tiền Huê Hồng: ' + str(hoahong) + ' Đồng'
        ketqua += '\n' + 'Tiền Lương Thực Lĩnh: ' + str(luongthang) + ' Đồng'
        self.ui.label_7.setText(ketqua)

    def TiepTuc(self):
        self.ui.lineEdit_5.setText(None)
        self.ui.lineEdit_3.setText(None)
        self.ui.lineEdit_2.setText(None)
        self.ui.lineEdit.setText(None)
        self.ui.lineEdit_4.setText(None)
        self.ui.label_7.setText(None)
        pos = self.mapFromGlobal(self.ui.lineEdit_2.pos())
        pos1 = abs(pos.x() - 475)
        pos2 = abs(pos.y() - 80)
        QCursor.setPos(pos1, pos2)
        self.ui.lineEdit_2.setFocus()

    def Thoat(self):
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())