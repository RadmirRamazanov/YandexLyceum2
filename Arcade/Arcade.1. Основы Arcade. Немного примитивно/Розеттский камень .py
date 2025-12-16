import arcade

from pyglet.graphics import Batch

DEFAULT_FONT_SIZE = 40
SCREEN_TITLE = "Rosetta Stone"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, lines, colors, font_size):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.batch = Batch()
        self.lines = lines
        self.colors = colors
        self.font_size = font_size

    def on_draw(self):
        self.clear()
        positions = [(300, 300), (300, 200), (300, 100)]
        positions.reverse()
        self.text1 = arcade.Text(
            self.lines[0],
            positions[0][0],
            positions[0][1],
            tuple(self.colors[0]),
            self.font_size,
            font_name="Arial",
            anchor_x="center",
            anchor_y="center"
        )

        self.text2 = arcade.Text(
            self.lines[1],
            positions[1][0],
            positions[1][1],
            tuple(self.colors[1]),
            self.font_size,
            font_name="Arial",
            anchor_x="center",
            anchor_y="center"
        )

        self.text3 = arcade.Text(
            self.lines[2],
            positions[2][0],
            positions[2][1],
            tuple(self.colors[2]),
            self.font_size,
            font_name="Arial",
            anchor_x="center",
            anchor_y="center"
        )
        self.text1.draw()
        self.text2.draw()
        self.text3.draw()


def setup_game(width=600, height=400, title="Rosetta", lines=None, colors=None, font_size=40):
    lines = lines or ["Ροζέτα Στόουν", "Rosetta stone", "حجر رشيد"]
    colors = colors or [[255, 3, 62], [153, 102, 204], [164, 198, 57]]

    game = MyGame(width, height, title, lines, colors, font_size)
    return game


def main():
    setup_game(
        600, 400, SCREEN_TITLE, ["Ροζέτα Στόουν", "Rosetta stone", "حجر رشيد"],
        [[255, 3, 62], [153, 102, 204], [164, 198, 57]], DEFAULT_FONT_SIZE
    )
    arcade.run()


if __name__ == "__main__":
    main()