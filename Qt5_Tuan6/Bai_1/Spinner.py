
from PyQt5.QtWidgets import QDialog, QApplication

from demoSpinner import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBoxSugarWeight.editingFinished.connect(self.result2)
        self.show()
    def bookPrice(self):
        return self.bookPrice()
    def result1(self):
        if len(self.ui.lineEditBookPrice.text()) !=0:
            bookPrice = int(self.ui.lineEditBookPrice.text())
        else:
            bookPrice = 0
            totalBookAmount = self.ui.spinBoxBookQty.value() * bookPrice
            self.ui.lineEditBookAmount.setText(str(totalBookAmount))
    def result2(self):
        if len(self.ui.lineEditSugarPrice.text()) !=0:
            sugarPrice = float(self.ui.lineEditSugarPrice.text())
        else:
            sugarPrice = 0
            totalSugarAmount = set.ui.doubleSpinBoxSugarWeight.value() * sugarPrice
            self.ui.lineEditSugarAmount.setText(str(round(totalSugarAmount,2)))
            totalBookAmount = int(self.ui.lineEditBookAmount.text())
            totalAmount = totalBookAmount + totalSugarAmount
            self.ui.labelAmount.setText(str(round(totalAmount,2)))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    windows = MyForm()
    windows.show()
    sys.exit(app.exec_())
