'''
Thực hiện add các item sau vào combobox:
+ Saving Account
+ Current Account
+ Recurring Desposit Account
+ Fixed Desposit Account
Yêu cầu: Người dùng chọn item tương ứng trong combobox sẽ hiển thị thông tin bên dưới
Label.
'''

# import thu vien PyQt5

from PyQt5.QtWidgets import *
from filee import *

#start
class Pyy3(QDialog):
    def __init__(self):
        super(Pyy3, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.Pyy)
    def Pyy(self):
        self.ui.label_2.setText("You have salect" + self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))

#end
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Pyy3()
    w.show()
    sys.exit(app.exec_())