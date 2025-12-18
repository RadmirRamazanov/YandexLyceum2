import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setMouseTracking(True)
        self.button = QPushButton(self)
        self.button.setText('Поймай меня')

    def mouseMoveEvent(self, event):
        x, y = [event.pos().x(), event.pos().y()]
        x_btn, y_btn = self.button.x(), self.button.y()
        while x in [i for i in range(x_btn - 5, x_btn + 6 + self.button.width())]:
            x_btn = random.randint(0, 500 - self.button.width())
        while y in [i for i in range(y_btn - 5, y_btn + 6 + self.button.height())]:
            y_btn = random.randint(0, 500 - self.button.height())
        self.button.move(x_btn, y_btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MyWidget()
    program.show()
    sys.exit(app.exec())