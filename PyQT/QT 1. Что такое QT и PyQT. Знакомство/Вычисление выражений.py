import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.counter = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(100, 100)
        self.trick_button.clicked.connect(self.nums)
        self.first_value = QLineEdit(self)
        self.first_value.move(10, 70)
        self.second_value = QLineEdit(self)
        self.second_value.move(150, 70)

    def nums(self):
        if self.counter % 2 == 0:
            num = self.first_value.text()
            self.second_value.setText(str(eval(num)))
        else:
            num = self.second_value.text()
            self.first_value.setText(str(eval(num)))
        self.counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())