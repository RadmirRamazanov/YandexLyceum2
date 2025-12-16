import arcade
from arcade.types import Color

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Color points"
COLORS = ['#ffc000', '#dc00a9', '#0065ac', '#22ad00']


class MyGame(arcade.Window):
    def __init__(self, width, height, title, colors):
        super().__init__(width, height, title)
        # Сохраните переданные цвета в атрибут класса
        self.colors = colors
        self.counter = 0

    def setup(self):
        self.points = []
        self.radius = 20

    def on_draw(self):
        self.clear()
        # В цикле отрисуйте все круги из self.points,
        # чередуя цвета из сохраненного списка
        for i in self.points:
            color = self.colors[i[2] % len(self.colors)].lstrip("#")
            color = (
                int(color[0:2], 16),
                int(color[2:4], 16),
                int(color[4:6], 16)
            )
            arcade.draw_circle_filled(i[0], i[1], self.radius, color)

    def on_mouse_press(self, x, y, button, modifiers):
        # Добавьте координаты (x, y) в self.points
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.points.append((x, y, self.counter))
            self.counter += 1


def setup_game(width=800, height=600, title="Color points", colors=None):
    # Если в функцию не передали список цветов, используйте COLORS по умолчанию
    game = MyGame(width, height, title, COLORS[:] if colors is None else colors)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
