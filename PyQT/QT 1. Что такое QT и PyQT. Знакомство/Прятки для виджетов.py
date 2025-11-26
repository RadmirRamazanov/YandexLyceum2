import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QCheckBox


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 360, 150)
        self.setWindowTitle("")
        self.edit1 = QLineEdit(self)
        self.edit1.move(70, 10)
        self.edit2 = QLineEdit(self)
        self.edit2.move(70, 40)
        self.edit3 = QLineEdit(self)
        self.edit3.move(70, 70)
        self.edit4 = QLineEdit(self)
        self.edit4.move(70, 100)
        self.checkbox1 = QCheckBox(self)
        self.checkbox1.move(40, 15)
        self.checkbox2 = QCheckBox(self)
        self.checkbox2.move(40, 45)
        self.checkbox3 = QCheckBox(self)
        self.checkbox3.move(40, 75)
        self.checkbox4 = QCheckBox(self)
        self.checkbox4.move(40, 105)
        self.checkbox1.setChecked(True)
        self.checkbox2.setChecked(True)
        self.checkbox3.setChecked(True)
        self.checkbox4.setChecked(True)
        self.checkbox1.toggled.connect(self.inf)
        self.checkbox2.toggled.connect(self.inf)
        self.checkbox3.toggled.connect(self.inf)
        self.checkbox4.toggled.connect(self.inf)

    def inf(self, checked):
        sender = self.sender()
        if sender == self.checkbox1:
            self.edit1.setVisible(checked)
        elif sender == self.checkbox2:
            self.edit2.setVisible(checked)
        elif sender == self.checkbox3:
            self.edit3.setVisible(checked)
        elif sender == self.checkbox4:
            self.edit4.setVisible(checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())