import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser


class Shuffle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 250)
        self.button = QPushButton(self)
        self.button.setText("Загрузить строки")
        self.button.move(5, 5)
        self.button.clicked.connect(self.load_strings)
        self.text_field = QTextBrowser(self)
        self.text_field.setMinimumSize(200, 200)
        self.text_field.move(5, 40)

    def load_strings(self):
        with open("lines.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            lst = []
            for i in range(len(lines)):
                if i % 2 == 1:
                    lst.append(lines[i])
            for i in range(len(lines)):
                if i % 2 == 0:
                    lst.append(lines[i])
            for i in lst:
                self.text_field.append(i[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Shuffle()
    ex.show()
    sys.exit(app.exec())