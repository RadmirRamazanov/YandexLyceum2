import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class UfoControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.x = 0
        self.y = 0
        self.ufo = QLabel(self)
        pixmap = QPixmap("ufo.png")
        self.ufo.setPixmap(pixmap)
        self.ufo.setGeometry(self.x, self.y, pixmap.width(), pixmap.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Up:
            if self.ufo.y() - 10 < 0:
                self.ufo.move(self.ufo.x(), 250)
            else:
                self.ufo.move(self.ufo.x(), self.ufo.y() - 10)
        elif event.key() == Qt.Key.Key_Down:
            if self.ufo.y() + 10 > 250:
                self.ufo.move(self.ufo.x(), 0)
            else:
                self.ufo.move(self.ufo.x(), self.ufo.y() + 10)
        elif event.key() == Qt.Key.Key_Left:
            if self.ufo.x() - 10 < 0:
                self.ufo.move(250, self.ufo.y())
            else:
                self.ufo.move(self.ufo.x() - 10, self.ufo.y())
        elif event.key() == Qt.Key.Key_Right:
            if self.ufo.x() + 10 > 250:
                self.ufo.move(0, self.ufo.y())
            else:
                self.ufo.move(self.ufo.x() + 10, self.ufo.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UfoControl()
    window.show()
    sys.exit(app.exec())