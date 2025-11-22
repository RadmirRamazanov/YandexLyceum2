import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class WidgetArt(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.matrix = matrix
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("")
        self.widgetArt = QGridLayout(self)
        self.setLayout(self.widgetArt)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                btn = QPushButton(self)
                btn.setFixedSize(30, 30)
                if self.matrix[i][j]:
                    btn.setText("*")
                self.widgetArt.addWidget(btn, i, j)