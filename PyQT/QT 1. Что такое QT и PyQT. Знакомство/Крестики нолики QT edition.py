import sys
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton,
                             QPushButton, QGridLayout, QApplication)
from PyQt6.QtCore import Qt


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.result = None
        self.button_grid = []
        self.c = 'X'
        self.d = False
        self.initUI()

    def initUI(self):
        w = QWidget()
        self.setCentralWidget(w)
        v = QVBoxLayout(w)
        p = QWidget()
        h = QHBoxLayout(p)
        h.addWidget(QLabel("Первый игрок:"))
        self.x_radio = QRadioButton("X")
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.radio_toggle)
        self.o_radio = QRadioButton("O")
        h.addWidget(self.x_radio)
        h.addWidget(self.o_radio)
        h.addStretch()
        v.addWidget(p)
        g = QWidget()
        g.setFixedSize(300, 300)
        x = QGridLayout(g)
        self.button_grid = []
        for i in range(3):
            t = []
            for j in range(3):
                b = QPushButton("")
                b.setFixedSize(90, 90)
                f = b.font()
                f.setPointSize(40)
                b.setFont(f)
                b.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                x.addWidget(b, i, j)
                t.append(b)
            self.button_grid.append(t)
        v.addWidget(g, 0, Qt.AlignmentFlag.AlignCenter)
        self.result = QLabel("")
        f = self.result.font()
        f.setPointSize(16)
        self.result.setFont(f)
        v.addWidget(self.result, 0, Qt.AlignmentFlag.AlignCenter)
        self.new_game_button = QPushButton("Новая игра")
        self.new_game_button.clicked.connect(self.new_game)
        v.addWidget(self.new_game_button, 0, Qt.AlignmentFlag.AlignCenter)
        self.setWindowTitle("Крестики-нолики")
        self.setFixedSize(400, 500)

    def make_move(self, i, j):
        if self.d or self.button_grid[i][j].text():
            return
        self.button_grid[i][j].setText(self.c)
        if self.check_win():
            self.result.setText(f"Выиграл {self.c}!")
            self.d = True
            self.block_all_buttons()
        elif self.is_full():
            self.result.setText("Ничья!")
            self.d = True
            self.block_all_buttons()
        else:
            self.c = 'O' if self.c == 'X' else 'X'

    def check_win(self):
        b = self.button_grid
        for i in range(3):
            if b[i][0].text() == b[i][1].text() == b[i][2].text() != "":
                return True
            if b[0][i].text() == b[1][i].text() == b[2][i].text() != "":
                return True
        if b[0][0].text() == b[1][1].text() == b[2][2].text() != "":
            return True
        if b[0][2].text() == b[1][1].text() == b[2][0].text() != "":
            return True
        return False

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if not self.button_grid[i][j].text():
                    return False
        return True

    def block_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.button_grid[i][j].setEnabled(False)

    def new_game(self):
        self.c = 'X' if self.x_radio.isChecked() else 'O'
        self.d = False
        self.result.setText("")
        for i in range(3):
            for j in range(3):
                self.button_grid[i][j].setText("")
                self.button_grid[i][j].setEnabled(True)

    def radio_toggle(self):
        self.new_game()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())