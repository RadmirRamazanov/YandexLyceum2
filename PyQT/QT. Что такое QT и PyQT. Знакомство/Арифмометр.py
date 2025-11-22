import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle("")
        self.first_value = QLineEdit(self)
        self.first_value.resize(40, 20)
        self.first_value.move(10, 10)
        self.first_value.setText('0')
        self.second_value = QLineEdit(self)
        self.second_value.resize(40, 20)
        self.second_value.move(110, 10)
        self.second_value.setText('0')
        self.result = QLineEdit(self)
        self.result.resize(40, 20)
        self.result.move(160, 10)
        self.result.setText('0')
        self.add_button = QPushButton(self)
        self.add_button.setText("+")
        self.add_button.resize(20, 20)
        self.add_button.move(50, 10)
        self.add_button.clicked.connect(self.add)
        self.substract_button = QPushButton(self)
        self.substract_button.setText("-")
        self.substract_button.resize(20, 20)
        self.substract_button.move(70, 10)
        self.substract_button.clicked.connect(self.sub)
        self.multiply_button = QPushButton(self)
        self.multiply_button.setText("*")
        self.multiply_button.resize(20, 20)
        self.multiply_button.move(90, 10)
        self.multiply_button.clicked.connect(self.mul)

    def add(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def sub(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def mul(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())