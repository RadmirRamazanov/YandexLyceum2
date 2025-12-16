import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smile Silence"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.radius = radius

    def on_draw(self):
        """Этот метод отвечает за отрисовку содержимого окна"""
        self.clear()
        arcade.draw_circle_filled(self.width // 2, self.height // 2, self.radius, (255, 192, 0))
        arcade.draw_circle_filled(self.width // 2 + self.radius // 2, self.height // 2 + self.radius // 2, 15, arcade.color.BLACK)
        arcade.draw_circle_filled(self.width // 2 - self.radius // 2, self.height // 2 + self.radius // 2, 15, arcade.color.BLACK)
        arcade.draw_arc_outline(self.width // 2, self.height // 2,
                                self.radius * 3 // 2, self.radius * 3 // 2, arcade.color.BLACK,
                                180, 360, max(1, self.radius // 20), 0)


def setup_game(width=800, height=600, title="Smile Silence", radius=200):
    game = MyGame(width, height, title, radius)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()