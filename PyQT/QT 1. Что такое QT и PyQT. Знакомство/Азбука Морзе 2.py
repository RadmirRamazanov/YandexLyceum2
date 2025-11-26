import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 360, 100)
        self.setWindowTitle("")
        self.result = QLineEdit(self)
        self.result.resize(350, 20)
        self.result.move(5, 60)
        self.alphabet_buttons = {}
        self.alp = list("abcdefghijklmnopqrstuvwxyz")
        self.m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "---", ".--.", "--.-", ".-.",
                  "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        x, y = 5, 5
        for i in self.alp:
            self.btn = QPushButton(self)
            self.btn.setText(i)
            self.btn.resize(25, 25)
            self.btn.move(x, y)
            x += 25
            if i == "n":
                y += 25
                x = 5
            self.alphabet_buttons[i] = self.btn
            self.btn.clicked.connect(lambda a, x=i: self.morze(x))

    def morze(self, i):
        self.result.insert(self.m[self.alp.index(self.alphabet_buttons[i].text())])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())