from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    # root widget
    def calculate(self):
        answer = eval(self.display.text)
        self.display.text = str(answer)

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()