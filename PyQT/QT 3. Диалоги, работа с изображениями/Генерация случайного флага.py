import copy
import random
import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class RandomFlag(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dr = None
        self.base = [80, 80, 120, 30]

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Генерация флага')
        self.button = QPushButton(self)
        self.button.move(20, 40)
        self.button.setText("Ввести количество цветов флага")
        self.button.clicked.connect(self.run)

    def run(self):
        i, okBtnPressed = QInputDialog.getInt(
            self,
            "Введите число цветов флага",
            "Сколько цветов?", 3, 1, 10, 1)
        if okBtnPressed:
            self.dr = i
            self.update()

    def paintEvent(self, event):
        if self.dr:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        base = copy.copy(self.base)
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(self.base[0], self.base[1], self.base[2], self.base[3] * self.dr)
        for i in range(self.dr):
            rand_color = QColor(random.randrange(256), random.randrange(256), random.randrange(256))
            qp.setBrush(rand_color)
            qp.drawRect(*base)
            base[1] += 30
        self.dr = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec())