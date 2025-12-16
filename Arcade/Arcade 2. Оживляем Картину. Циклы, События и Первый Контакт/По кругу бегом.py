import math

import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Rounding circle"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        # Создайте атрибуты для хранения текущего угла поворота и скорости вращения.
        self.angle = 0.0
        self.radius = 20
        self.orbit_radius = 100
        self.velocity = 0.0
        self.x = self.width // 2
        self.y = self.height // 2

    def on_draw(self):
        self.clear()
        # Вычислите x и y круга, используя math.sin и math.cos от текущего угла.
        # Не забудьте прибавить смещение к центру окна.
        # Затем отрисуйте круг в этих координатах.
        x = self.x + self.orbit_radius * math.cos(self.angle)
        y = self.y + self.orbit_radius * math.sin(self.angle)
        arcade.draw_circle_filled(x, y, self.radius, arcade.color.YELLOW)

    def on_update(self, delta_time):
        # На каждом кадре обновляйте текущий угол, прибавляя к нему текущую скорость.
        self.angle += self.velocity

    def on_key_press(self, key, modifiers):
        # В зависимости от нажатой стрелки, изменяйте скорость вращения на 0.01.
        if key == arcade.key.RIGHT:
            self.velocity += 0.01
        elif key == arcade.key.LEFT:
            self.velocity -= 0.01


def setup_game(width=800, height=600, title="Rounding circle"):
    game = MyGame(width, height, title)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()