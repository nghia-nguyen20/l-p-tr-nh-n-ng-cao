'''
thứ 5 ngày 17 tháng 12 năm 2020 LTNC
Thiết kế List Widget chứa các item sau:
+ Urine Analasis $5
+ Chest X Ray 100$
+ Sugar Level test $3
+ Hemoglobin test $7
+ Thyroid Stumulating Harmone test $10
Yêu Cầu: Người dùng chọn item nào sẽ hiển thị thông tin item đó xuống Label “You have
selected:….”
'''
# import thu vien PyQt5
from PyQt5.QtWidgets import *
from listwidget1 import *

#start
class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidget.itemClicked.connect(self.Pyy)
#ham tinh toan
    def Pyy(self):
        self.ui.label_2.setText("you have selected " + self.ui.listWidget.currentItem().text())
#end
if __name__ == "__main__":
    import sys
    app=QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())