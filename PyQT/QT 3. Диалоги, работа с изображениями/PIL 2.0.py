import sys
from PyQt6.QtGui import QImage, QTransform, QColor, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QButtonGroup
from PyQt6.QtCore import Qt


SCREEN_SIZE = [500, 500]


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.channelButtons = QButtonGroup(self)
        self.rotateButtons = QButtonGroup(self)
        self.btn1 = QPushButton("R", self)
        self.btn1.move(10, 50)
        self.btn1.clicked.connect(self.color)
        self.btn2 = QPushButton("G", self)
        self.btn2.move(10, 120)
        self.btn2.clicked.connect(self.color)
        self.btn3 = QPushButton("B", self)
        self.btn3.move(10, 190)
        self.btn3.clicked.connect(self.color)
        self.btn4 = QPushButton("ALL", self)
        self.btn4.move(10, 260)
        self.btn4.clicked.connect(self.color)
        self.btn5 = QPushButton("Против часовой стрелки", self)
        self.btn5.move(10, 400)
        self.btn5.resize(200, 50)
        self.btn5.clicked.connect(self.trans)
        self.btn6 = QPushButton("По часовой стрелке", self)
        self.btn6.move(250, 400)
        self.btn6.resize(200, 50)
        self.btn6.clicked.connect(self.trans)
        self.channelButtons.addButton(self.btn1)
        self.channelButtons.addButton(self.btn2)
        self.channelButtons.addButton(self.btn3)
        self.channelButtons.addButton(self.btn4)
        self.rotateButtons.addButton(self.btn5)
        self.rotateButtons.addButton(self.btn6)
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.original_image = QImage(fname)
        self.curr_image = self.original_image.copy()  # Добавляем обязательное поле curr_image
        self.current_color_filter = None
        self.rotation_angle = 0
        self.image = QLabel(self)
        self.image.move(150, 30)
        self.image.resize(350, 350)
        self.update_image_display()

    def update_image_display(self):
        result_image = self.original_image.copy()
        if self.current_color_filter:
            width = result_image.width()
            height = result_image.height()
            for i in range(width):
                for j in range(height):
                    color = result_image.pixelColor(i, j)
                    r, g, b, a = color.getRgb()
                    if self.current_color_filter == 'R':
                        result_image.setPixelColor(i, j, QColor(r, 0, 0))
                    elif self.current_color_filter == 'G':
                        result_image.setPixelColor(i, j, QColor(0, g, 0))
                    elif self.current_color_filter == 'B':
                        result_image.setPixelColor(i, j, QColor(0, 0, b))
        if self.rotation_angle != 0:
            transform = QTransform().rotate(self.rotation_angle)
            result_image = result_image.transformed(transform)
        self.curr_image = result_image
        scaled_image = result_image.scaled(
            self.image.width(),
            self.image.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        pixmap = QPixmap.fromImage(scaled_image)
        self.image.setPixmap(pixmap)

    def color(self):
        sender = self.sender()
        if sender == self.btn1:
            self.current_color_filter = 'R'
        elif sender == self.btn2:
            self.current_color_filter = 'G'
        elif sender == self.btn3:
            self.current_color_filter = 'B'
        elif sender == self.btn4:
            self.current_color_filter = None
        self.update_image_display()

    def trans(self):
        sender = self.sender()
        if sender == self.btn5:
            self.rotation_angle = (self.rotation_angle - 90) % 360
        else:
            self.rotation_angle = (self.rotation_angle + 90) % 360
        self.update_image_display()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())