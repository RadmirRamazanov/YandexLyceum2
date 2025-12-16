import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Perspective"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, width_rect, height_rect, color_rect: tuple[int, int, int]):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.width_rect = width_rect
        self.height_rect = height_rect
        self.color_rect = color_rect

    def on_draw(self):
        self.clear()
        color_rect2 = (self.color_rect[0] - 20, self.color_rect[1] - 20, self.color_rect[2])
        color_rect3 = (self.color_rect[0] - 40, self.color_rect[1] - 40, self.color_rect[2])
        color_rect4 = (self.color_rect[0] - 60, self.color_rect[1] - 60, self.color_rect[2])
        arcade.draw_lbwh_rectangle_filled((self.width - self.width_rect + 120) // 2, 200, self.width_rect - 120,
                                          self.height_rect - 120, color_rect4)
        arcade.draw_lbwh_rectangle_filled((self.width - self.width_rect + 80) // 2, 140, self.width_rect - 80,
                                          self.height_rect - 80, color_rect3)
        arcade.draw_lbwh_rectangle_filled((self.width - self.width_rect + 40) // 2, 80, self.width_rect - 40,
                                          self.height_rect - 40, color_rect2)
        arcade.draw_lbwh_rectangle_filled((self.width - self.width_rect) // 2, 20,
                                          self.width_rect, self.height_rect, self.color_rect)



def setup_game(width=900, height=600, title="Perspective", width_rect=500, height_rect=300, color_rect=(192, 255, 0)):
    game = MyGame(width, height, title, width_rect, height_rect, color_rect)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()