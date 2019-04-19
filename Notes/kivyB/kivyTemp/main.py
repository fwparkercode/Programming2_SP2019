import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Window.size = (600, 400)

class TempApp(App):
    def build(self):
        return TempLayout()

class TempLayout(BoxLayout):
    # will contain all of my functions
    def f_conversion(self):
        if self.temp.text == "":
            return
        else:
            f = float(self.temp.text) * 9 / 5 + 32
            self.answer.text = str(f)
    def c_conversion(self):
        if self.temp.text == "":
            return
        else:
            c = (float(self.temp.text) - 32) * 5 / 9
            self.answer.text = str(c)

if __name__ == "__main__":
    app = TempApp()
    app.run()