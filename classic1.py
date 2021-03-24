import sys

from PySide2.QtWidgets import QApplication, QWidget, QDialog
from  PySide2 import  QtGui
from classic import Ui_Dialog



class UI(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(dialog)

        self.ui.comboBox.addItem("400- ......")
        self.ui.comboBox.addItem("400- ...... -400")
        self.ui.comboBox.addItem("500- ......")
        self.ui.comboBox.addItem("500- ...... -500")
        self.ui.comboBox.addItem("600- ......")
        self.ui.comboBox.addItem("600- ...... -600")

        self.ui.comboBox_3.addItem("KAKSI OVINEN")
        self.ui.comboBox_3.addItem("KOLMI OVINEN")

        self.ui.comboBox_4.addItem("100")
        self.ui.comboBox_4.addItem("50 / 50")
        self.ui.comboBox_4.addItem("33 / 33 / 33")
        self.ui.comboBox_4.addItem("40 / 20 / 40")

        tabeli näitamine

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    prog = UI(dialog)
    dialog.show()
    sys.exit(app.exec_())