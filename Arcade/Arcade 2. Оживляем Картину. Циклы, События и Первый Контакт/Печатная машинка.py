import arcade
from pyglet.graphics import Batch

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Writing Machine"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.batch = Batch()
        # Создайте атрибут для хранения набираемого текста (изначально пустую строку).
        self.text = ""

    def on_key_press(self, key, modifiers):
        # 1. Преобразуйте код клавиши (key) в символ.
        # 2. Проверьте параметр modifiers, чтобы определить, нажат ли Shift.
        # 3. Добавьте полученный символ (в нужном регистре) к вашей текстовой строке.
        if modifiers == arcade.key.MOD_SHIFT:
            if chr(key).isalpha():
                self.text += chr(key).upper()
        else:
            self.text += chr(key)

    def on_draw(self):
        self.clear()
        # Создайте объект arcade.Text с текущим текстом и нужными параметрами.
        # Для точного центрирования используйте anchor_x="center" и anchor_y="center".
        # Не забудьте отрисовать batch.
        text = arcade.Text(
            self.text,
            self.width // 2,
            self.height // 2,
            arcade.color.BANANA_YELLOW,
            100,
            font_name="Calibri",
            batch=self.batch,
            anchor_x="center",
            anchor_y="center"
        )
        self.batch.draw()

def setup_game(width=800, height=600, title="Writing Machine"):
    game = MyGame(width, height, title)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
