import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6 import QtGui, QtCore


class Cirtcles(QWidget):
    def __init__(self):
        super().__init__()
        self.f = None

    def paintEvent(self, ev):
        if not self.f:
            return
        pnt = QtGui.QPainter(self)
        pnt.setBrush(QtGui.QBrush(self.f['c']))
        pnt.drawEllipse(self.f['pos'], self.f['r'], self.f['r'])

    def balls(self):
        r = random.randint(20, 100)
        c = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.f = {'pos': QtCore.QPoint(random.randint(50, 600), random.randint(50, 300)), 'r': r, 'c': c}
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 350)
        self.initUI()

    def initUI(self):
        self.widget = Cirtcles()
        self.setCentralWidget(self.widget)
        self.pushButton = QPushButton(self)
        self.pushButton.move(250, 250)
        self.pushButton.setText("Golden Balls")
        self.pushButton.clicked.connect(self.widget.balls)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
