from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400) # change the default size

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    # all my functions go in here (root widget)
    def calculate(self, equation):
        answer = eval(equation)
        self.display.text = str(answer)

if __name__ == "__main__":
    #my_equation = "2+3*(3)**2"
    #print(eval(my_equation))

    app = CalculatorApp()
    app.run()

