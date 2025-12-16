import arcade
from pyglet.graphics import Batch

SCREEN_WIDTH, SCREEN_HEIGHT = 200, 200
TITLE = "Start"
FONT = 80


class MyGame(arcade.Window):
    def __init__(self, width, height, title, font):
        super().__init__(width, height, title)
        # Сохраните переданный размер шрифта в атрибут класса
        self.font = font

    def setup(self):
        self.batch = Batch()
        # Создайте атрибут для хранения оставшегося времени (начните с 10).
        # Запланируйте вызов метода update_timer каждую секунду с помощью arcade.schedule.
        self.timer = 10
        arcade.schedule(self.update_timer, 1)


    def update_timer(self, delta_time):
        # Уменьшайте оставшееся время на 1, если оно больше 0.
        if self.timer > 0:
            self.timer -= 1

    def on_draw(self):
        self.clear()
        # Создайте объект arcade.Text для отображения оставшегося времени.
        # Укажите правильные координаты, цвет, размер и центрирование (anchor).
        # Затем отрисуйте batch.
        self.text = arcade.Text(
            str(self.timer),
            self.width // 2,
            self.height // 2,
            arcade.color.RED,
            self.font,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch
        )
        self.batch.draw()


def setup_game(width=200, height=200, title="Start", font=80):
    game = MyGame(width, height, title, font)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
