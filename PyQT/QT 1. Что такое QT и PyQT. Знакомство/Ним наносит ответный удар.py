import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.moves_left = 10
        self.init_game()
        self.init_ui()

    def init_game(self):
        self.X = random.randint(10, 50)
        self.Y = random.randint(1, 10)
        self.Z = random.randint(1, 10)
        self.moves_left = 10

    def init_ui(self):
        self.setWindowTitle("Ним наносит ответный удар")
        self.label_x = QLabel(f"Текущее значение X: {self.X}")
        self.label_moves = QLabel(f"Осталось ходов: {self.moves_left}")
        self.result_label = QLabel("")
        self.btnp = QPushButton(f"+{self.Y}")
        self.btnm = QPushButton(f"-{self.Z}")
        self.btnp.clicked.connect(self.increase_x)
        self.btnm.clicked.connect(self.decrease_x)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label_x)
        v_layout.addWidget(self.label_moves)
        v_layout.addWidget(self.result_label)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btnp)
        h_layout.addWidget(self.btnm)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

    def update_labels(self):
        self.label_x.setText(f"Текущее значение X: {self.X}")
        self.label_moves.setText(f"Осталось ходов: {self.moves_left}")

    def check_game_over(self):
        if self.X == 0:
            self.result_label.setText("Поздравляем, вы выиграли!")
            self.restart_game()
        elif self.moves_left == 0:
            self.result_label.setText(f"Проигрыш! Не удалось привести X к 0."
                                      f"\nНачинаем новую игру.\nX={self.X}, Y={self.Y}, Z={self.Z}")
            self.restart_game()

    def restart_game(self):
        self.init_game()
        self.update_labels()
        self.btnp.setText(f"+{self.Y}")
        self.btnm.setText(f"-{self.Z}")

    def increase_x(self):
        if self.moves_left > 0:
            self.X += self.Y
            self.moves_left -= 1
            self.update_labels()
            self.check_game_over()

    def decrease_x(self):
        if self.moves_left > 0:
            self.X -= self.Z
            self.moves_left -= 1
            self.update_labels()
            self.check_game_over()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NimStrikesBack()
    window.show()
    sys.exit(app.exec())
