import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')
        self.setMouseTracking(True)
        self.pixmap = QPixmap('car1.png')
        self.lbl = QLabel(self)
        self.lbl.resize(self.pixmap.size())
        self.lbl.setPixmap(self.pixmap)
        self.cur = ['car1.png', 'car2.png', 'car3.png']
        self.counter = 0

    def mouseMoveEvent(self, event):
        if event.pos().x() <= 250 and event.pos().y() <= 250:
            self.lbl.move(event.pos().x(), event.pos().y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.counter += 1
            if self.counter > 2:
                self.counter = 0
            self.pixmap = QPixmap(self.cur[self.counter])
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())