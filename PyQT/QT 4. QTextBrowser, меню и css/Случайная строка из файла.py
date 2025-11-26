import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QVBoxLayout


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.layout = QVBoxLayout(self)
        self.button = QPushButton(self)
        self.layout.addWidget(self.button)
        self.button.setText("Вывести")
        self.button.clicked.connect(self.load_random_string)
        self.textBrowser = QTextBrowser(self)
        self.layout.addWidget(self.textBrowser)

    def load_random_string(self):
        try:
            with open("lines.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                try:
                    html_text = f"""
                    <h1>{random.choice(lines)}<h1>
                    """
                    self.textBrowser.setHtml(html_text)
                except IndexError:
                    self.textBrowser.setText("")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())