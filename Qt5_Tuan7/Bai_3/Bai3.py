'''
Yêu cầu:
+ Nhập giá trị item vào textbox, nhấn Add sẽ hiển thị qua List
+ Người dùng chọn item trong List và nhấn các tùy chon như Edit sẽ hiển thị ra
Dialog tương ứng cho người dùng nhập lại thông tin cần Edit (hình b)
+ Chọn item nhấn Delete sẽ xóa item tương ứng
+ Nhấn Delete All sẽ xóa tất cả item trong List
'''
# import thu vien PyQt5

from PyQt5.QtWidgets import *
from List import *

#start
class Pyy2(QDialog):
    def __init__(self):
        super(Pyy2, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.Pyy)
        self.ui.Add_3.clicked.connect(self.Delete)
        self.ui.Add_4.clicked.connect(self.DeleteAll)
        self.ui.Add_2.clicked.connect(self.Edit)
#ham tinh
    def Pyy(self):
        if len(self.ui.lineEdit.text()) != 0:
            self.ui.listWidget.addItem(str(" ".join(self.ui.lineEdit.text().split())))
    def Delete(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    def DeleteAll(self):
        self.ui.listWidget.clear()
    def Edit(self):
        row = self.ui.listWidget.currentRow()
        new, ok = QInputDialog.getText(self, "Enter new text", " nhap gia tri")
        if ok and (len(new) != 0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row, QListWidgetItem(new))
#end
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Pyy2()
    w.show()
    sys.exit(app.exec_())