import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Drop balls"
VELOCITY = 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        # Сохраните переданную скорость в атрибут класса
        self.velocity = velocity

    def setup(self):
        # Список для хранения координат [x, y] каждого шарика
        self.points = []
        # Параллельный список для хранения скоростей [dx, dy] каждого шарика
        self.speed = []
        # Задайте радиус шариков
        self.radius = 20

    def on_draw(self):
        self.clear()
        # В цикле для каждого шарика:
        # 1. Проверьте столкновение со стенами и инвертируйте скорость по нужной оси.
        # 2. Обновите координаты шарика, используя его скорость.
        # 3. Отрисуйте шарик в новых координатах.
        for idx in range(len(self.points)):
            x, y = self.points[idx]
            dx, dy = self.speed[idx]
            if self.width - self.radius < x or x - self.radius < 0:
                dx *= -1
            if self.height - self.radius < y or y - self.radius < 0:
                dy *= -1
            x -= dx
            y += dy
            self.points[idx] = [x, y]
            self.speed[idx] = [dx, dy]
            arcade.draw_circle_filled(x, y, self.radius, arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        # При клике добавьте в self.points координаты нового шарика,
        # а в self.speed — его начальную скорость.
        self.points.append([x, y])
        self.speed.append([self.velocity, self.velocity])


def setup_game(width=800, height=600, title="Drop balls", velocity=2):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
