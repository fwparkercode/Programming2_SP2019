import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (800, 100)


class AddLayout(BoxLayout):
    def calculate(self):
        self._answer.text = str(eval(self._n1.text + "+" + self._n2.text))


class AddingApp(App):
    def build(self):
        return AddLayout()

if __name__ == "__main__":
    adding_app = AddingApp()
    adding_app.run()