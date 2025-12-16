import arcade
from arcade.types import Color

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying squares"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, side, color):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.side = side
        color = color.lstrip("#")
        self.color = (
            int(color[0:2], 16),
            int(color[2:4], 16),
            int(color[4:6], 16)
        )

    def setup(self):
        self.points = [[(self.width - self.side) // 2, 0, self.side, self.color, 2, 2],
                       [(self.width - self.side) // 2, 0, self.side, self.color, -2, 2]]  # Список списков координат квадратов для рисования

    def on_draw(self):
        """Этот метод отвечает за отрисовку содержимого окна"""
        self.clear()
        arcade.draw_lbwh_rectangle_filled(
            self.points[0][0], self.points[0][1], self.points[0][2], self.points[0][2], self.points[0][3]
        )
        arcade.draw_lbwh_rectangle_filled(
            self.points[1][0], self.points[1][1], self.points[1][2], self.points[1][2], self.points[1][3]
        )


    def on_update(self, delta_time):
        """Этот метод отвечает за обновление логики игры (анимации, взаимодействия и т. д.)"""
        self.points[0][0] += self.points[0][4]
        self.points[0][1] += self.points[0][5]
        self.points[1][0] += self.points[1][4]
        self.points[1][1] += self.points[1][5]


def setup_game(width=900, height=600, title="Flying squares", side=100, color="#ff40ff"):
    game = MyGame(width, height, title, side, color)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()