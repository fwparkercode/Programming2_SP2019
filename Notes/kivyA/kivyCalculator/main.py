from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (240, 320)

class CalcApp(App):
    def build(self):
        return CalcLayout()

class CalcLayout(BoxLayout):
    def calculate(self, equation):
        try:
            answer = str(eval(equation))
        except:
            answer = ""
        self.display.text = answer





if __name__ == "__main__":
    app = CalcApp()
    app.run()