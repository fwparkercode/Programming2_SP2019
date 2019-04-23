import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

equation = "3+5/7"
print(equation)
print("{:.2f}".format(eval(equation)))

class HypotenuseApp(App):
    def build(self):
        return HypotenuseLayout()

class HypotenuseLayout(BoxLayout):
    # all of my functions will be here
    def calculate(self):
        if self.leg1.text == "":
            return
        else:
            hyp = (float(self.leg1.text) ** 2 + float(self.leg2.text) ** 2) ** 0.5
            self.answer.text = "{:.2f}".format(hyp)

if __name__ == "__main__":
    app = HypotenuseApp()
    app.run()