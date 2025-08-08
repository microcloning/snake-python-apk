from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.core.window import Window

class SnakeGame(Widget):
    snake = ListProperty([[0, 0]])
    direction = ListProperty([10, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.1)

    def update(self, dt):
        head_x, head_y = self.snake[-1]
        new_head = [head_x + self.direction[0], head_y + self.direction[1]]
        self.snake.append(new_head)
        if len(self.snake) > 10:
            self.snake.pop(0)
        self.canvas.clear()
        with self.canvas:
            from kivy.graphics import Color, Rectangle
            Color(0, 1, 0)
            for segment in self.snake:
                Rectangle(pos=segment, size=(10, 10))

class SnakeApp(App):
    def build(self):
        Window.size = (300, 300)
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
