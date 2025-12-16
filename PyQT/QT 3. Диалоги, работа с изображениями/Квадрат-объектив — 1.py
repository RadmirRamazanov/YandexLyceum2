import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 900)
        self.setWindowTitle("Квадрат-объектив — 1")
        self.color = QColor(0, 0, 255)
        self.label_a = QLabel("Размер стороны (a)", self)
        self.label_a.move(50, 30)
        self.label_k = QLabel("Коэффициент масштабирования (k)", self)
        self.label_k.move(50, 70)
        self.label_n = QLabel("Количество (n)", self)
        self.label_n.move(50, 110)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(300, 25)
        self.lineEdit.setText("300")
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.move(300, 65)
        self.lineEdit_2.setText("0.9")
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.move(300, 105)
        self.lineEdit_3.setText("10")
        self.btn = QPushButton("Нарисовать", self)
        self.btn.move(400, 65)
        self.btn.clicked.connect(self.update)
        self.a = 300
        self.k = 0.9
        self.n = 10

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(self.color)
        try:
            a = int(self.lineEdit.text())
        except ValueError:
            a = 300
        try:
            k = float(self.lineEdit_2.text())
            if not (k < 1):
                k = 0.9
        except ValueError:
            k = 0.9
        try:
            n = int(self.lineEdit_3.text())
        except ValueError:
            n = 10
        self.a = a
        self.k = k
        self.n = n
        x0, y0 = 50, 130
        center_x = x0 + a / 2
        center_y = y0 + a / 2
        side = float(a)
        for _ in range(n):
            left = center_x - side / 2
            top = center_y - side / 2
            rect = QRectF(left, top, side, side)
            qp.drawRect(rect)
            side *= k


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec())
