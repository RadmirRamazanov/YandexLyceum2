import arcade

SCREEN_TITLE = "Origami Cat"
PART = 25


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BEIGE)
        self.part = part

    def on_draw(self):
        self.clear()
        arcade.draw_polygon_outline(
            ((self.part, self.part * 18), (self.part * 2, self.part * 12),
             (self.part * 4, self.part * 15), (self.part, self.part * 18)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 2, self.part * 12), (self.part * 4, self.part * 15),
             (self.part * 5, self.part * 15), (self.part * 5, self.part * 9),
             (self.part * 2, self.part * 12)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 4, self.part * 15), (self.part * 6, self.part * 15),
             (self.part * 8, self.part * 12), (self.part * 5, self.part * 9),
             (self.part * 5, self.part * 15)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 6, self.part * 15), (self.part * 9, self.part * 18),
             (self.part * 8, self.part * 12), (self.part * 6, self.part * 15)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 3, self.part * 11), (self.part * 5, self.part * 3),
             (self.part * 9, self.part * 3), (self.part * 11, self.part * 7),
             (self.part * 7, self.part * 11), (self.part * 5, self.part * 3)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 5, self.part * 9), (self.part * 5, self.part * 3)), arcade.color.COOL_BLACK, 4
        )
        arcade.draw_polygon_outline(
            ((self.part * 8, self.part), (self.part * 11, self.part * 7),
             (self.part * 11, self.part * 3), (self.part * 8, self.part)), arcade.color.COOL_BLACK, 4
        )


def setup_game(width=300, height=475, title="Origami Cat", part=25):
    game = MyGame(width, height, title, part)
    return game


def main():
    setup_game(PART * 12, PART * 19, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()
