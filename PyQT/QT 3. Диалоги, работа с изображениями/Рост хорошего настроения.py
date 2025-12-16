import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor


class GoodMoodRising(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1000)
        self.color = QColor(255, 0, 0)
        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setGeometry(970, 40, 20, 500)
        self.slider.valueChanged.connect(self.update)
        self.size = self.slider.value()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(self.color)
        qp.setBrush(Qt.BrushStyle.NoBrush)
        size = self.slider.value()
        qp.drawEllipse(0, 0, 10 * size, 10 * size)
        qp.drawEllipse(2 * size, 2 * size, 2 * size, 2 * size)
        qp.drawEllipse(10 * size - 4 * size, 2 * size, 2 * size, 2 * size)
        smile_rect = QRect(2 * size, 6 * size, 6 * size, 2 * size)
        qp.setBrush(Qt.BrushStyle.NoBrush)
        qp.drawArc(smile_rect, -480, -1920)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GoodMoodRising()
    window.show()
    sys.exit(app.exec())
