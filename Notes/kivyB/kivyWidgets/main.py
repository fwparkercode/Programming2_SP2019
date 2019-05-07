from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (400, 600)
Window.clearcolor = (1, 1, 1, 1)


class DemoApp(App):
    def build(self):
        return DemoLayout()

class DemoLayout(BoxLayout):
    def turn_on_lights(self, value):
        if value:
            Window.clearcolor = (1,1,1,1)
            self.switch_text.color = (0,0,0,1)
        else:
            Window.clearcolor = (0,0,0,1)
            self.switch_text.color = (1,1,1,1)

    def color_slide(self, value):
        self.slider_value.color = (value, value, value, 1)

    def spinner_clicked(self, text):
        print(text)

    def checked(self, active):
        print(active)

if __name__ == "__main__":
    demo = DemoApp()
    demo.run()