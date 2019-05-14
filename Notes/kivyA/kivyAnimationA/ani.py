from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.graphics import Color
import random

Window.size = [600, 600]

class AniApp(App):
    def build(self):
        return(AniLayout())

class AniLayout(Widget):
    def on_touch_down(self, touch):
        print(touch.x, touch.y)
        #self.ani_rect.center_x = touch.x
        #self.ani_rect.center_y = touch.y
        self.ani_rect.animated_move(touch.x, touch.y)


class ClockRect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60)
        self.speedx = 5
        self.speedy = 3

    def update(self, *args):
        self.x += self.speedx
        if self.right > Window.width or self.x < 0:
            self.speedx *= -1
            self.my_color = [random.random(),random.random(),random.random(),1]

        self.y += self.speedy
        if self.y < 0 or self.top > Window.height:
            self.speedy *= -1
            self.my_color = [random.random(), random.random(), random.random(), 1]


class AniRect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def animated_move(self, x, y):
        animation1 = Animation(center_x=x, center_y=y, d=1, t="out_bounce")
        Animation.cancel_all(self)
        animation1.start(self)

if __name__ == "__main__":
    app = AniApp()
    app.run()
