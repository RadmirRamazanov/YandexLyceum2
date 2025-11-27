import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtCore


class Cirtcles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.f = None
        self.pushButton.clicked.connect(self.balls)

    def paintEvent(self, ev):
        if not self.f:
            return
        pnt = QtGui.QPainter(self)
        pnt.setBrush(QtGui.QBrush(self.f['c']))
        pnt.drawEllipse(self.f['pos'], self.f['r'], self.f['r'])

    def balls(self):
        r = random.randint(20, 100)
        '''
        c = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        '''
        self.f = {'pos': QtCore.QPoint(random.randint(50, 600), random.randint(50, 600)), 'r': r, 'c': QtGui.QColor(255, 255, 0)}
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cirtcles()
    ex.show()
    sys.exit(app.exec())