import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('')
        self.calculate_button = QPushButton('->', self)
        self.calculate_button.move(100, 100)
        self.calculate_button.clicked.connect(self.nums)
        self.number_1 = QLineEdit(self)
        self.number_1.move(10, 70)
        self.number_2 = QLineEdit(self)
        self.number_2.move(150, 70)
        self.result_sum = QLCDNumber(self)
        self.result_sum.move(110, 130)
        self.result_sub = QLCDNumber(self)
        self.result_sub.move(110, 160)
        self.result_mul = QLCDNumber(self)
        self.result_mul.move(110, 190)
        self.result_div = QLCDNumber(self)
        self.result_div.move(110, 220)

    def nums(self):
        num1 = self.number_1.text()
        num2 = self.number_2.text()
        self.result_sum.display(str(int(num1) + int(num2)))
        self.result_sub.display(str(int(num1) - int(num2)))
        self.result_mul.display(str(int(num1) * int(num2)))
        try:
            self.result_div.display(str(round(float(num1) / float(num2), 3)))
        except ZeroDivisionError:
            self.result_div.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())