'''
Thực hiện add font vào combobox
Yêu cầu: người dùng gõ văn bản vào ô Type some text, sau đó chọn giá trị font
trên combobox, văn bản sẽ được format theo font người dùng chọn
'''

# import thu vien PyQt5

from PyQt5.QtWidgets import *
from file import *

#start
class Pyy4(QDialog):
    def __init__(self):
        super(Pyy4, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.fontComboBox.currentFontChanged.connect(self.Pyy)
    def Pyy(self):
        self.ui.textEdit.setFont(self.ui.fontComboBox.currentFont())
#end
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Pyy4()
    w.show()
    sys.exit(app.exec_())