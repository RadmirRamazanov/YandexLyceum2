import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Moving Square"
VELOCITY = 20


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        # Сохраните переданную скорость в атрибут класса
        self.velocity = velocity

    def setup(self):
        # Создайте атрибуты для хранения координат центра квадрата и его стороны
        self.points = [self.width // 2, self.height // 2]
        self.side = 100

    def on_draw(self):
        self.clear()
        # Отрисуйте квадрат, используя его текущие координаты и размеры
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.points[0], self.points[1], self.side, self.side),
            arcade.color.WHITE
        )

    def on_key_press(self, key, modifiers):
        # 1. В зависимости от нажатой стрелки, измените координаты центра квадрата.
        # 2. После изменения, проверьте каждую из четырех границ окна.
        # 3. Если квадрат вышел за границу, скорректируйте его координату так,
        #    чтобы он касался края окна.
        if key == arcade.key.UP:
            self.points[1] += self.velocity
        elif key == arcade.key.LEFT:
            self.points[0] -= self.velocity
        elif key == arcade.key.RIGHT:
            self.points[0] += self.velocity
        elif key == arcade.key.DOWN:
            self.points[1] -= self.velocity
        if self.points[1] + (self.side // 2) > self.height:
            self.points[1] = self.height - self.side // 2
        elif self.points[1] - (self.side // 2) < 0:
            self.points[1] = self.side // 2
        elif self.points[0] + (self.side // 2) > self.width:
            self.points[0] = self.width - self.side // 2
        elif self.points[0] - (self.side // 2) < 0:
            self.points[0] = self.side // 2


def setup_game(width=800, height=600, title="Moving Square", velocity=20):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()