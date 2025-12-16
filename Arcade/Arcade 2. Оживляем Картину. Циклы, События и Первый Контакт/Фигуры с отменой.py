import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Rects With Cancel"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        # Список для хранения всех нарисованных прямоугольников
        self.rects = []
        # Создайте переменные для хранения параметров текущего (рисуемого)
        # прямоугольника и флаг состояния "is_drawing".
        self.fx, self.fy, self.lx, self.ly = None, None, None, None
        self.is_drawing = False

    def on_draw(self):
        self.clear()
        # Отрисуйте все сохранённые прямоугольники из self.rects.
        # Также, если пользователь сейчас рисует новый прямоугольник, отрисуйте и его.
        for i in self.rects:
            x1, y1, x2, y2 = i
            left = min(x1, x2)
            right = max(x1, x2)
            bottom = min(y1, y2)
            top = max(y1, y2)
            arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, arcade.color.WHITE, 2)
        if self.is_drawing:
            left = min(self.fx, self.lx)
            right = max(self.fx, self.lx)
            bottom = min(self.fy, self.ly)
            top = max(self.fy, self.ly)
            arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, arcade.color.WHITE, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        # Зафиксируйте начальные координаты и активируйте флаг начала рисования.
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.fx, self.fy, self.lx, self.ly, self.is_drawing = x, y, x, y, True

    def on_mouse_motion(self, x, y, button, modifiers):
        # Если флаг рисования активен, обновляйте ширину и высоту
        # текущего прямоугольника на основе положения мыши.
        if self.is_drawing:
            self.lx, self.ly = x, y

    def on_mouse_release(self, x, y, button, modifiers):
        # Если рисование было активно, добавьте новый прямоугольник в список self.rects
        # и сбросьте флаг/временные переменные.
        if self.is_drawing:
            self.rects.append((self.fx, self.fy, x, y))
            self.fx, self.fy, self.lx, self.ly, self.is_drawing = None, None, None, None, False

    def on_key_press(self, key, modifiers):
        # Реализуйте отмену последнего действия: при нажатии Ctrl+Z
        # удаляйте последний элемент из списка self.rects.
        if key == arcade.key.Z and modifiers == arcade.key.MOD_CTRL:
            self.rects.pop()


def setup_game(width=800, height=600, title="Rects With Cancel"):
    game = MyGame(width, height, title)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
