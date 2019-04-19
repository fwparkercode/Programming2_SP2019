import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class HypotenuseApp(App):
    def build(self):
        return HypotenuseLayout()

class HypotenuseLayout(BoxLayout):
    # all of my functions will be here
    def calculate(self):
        print("It worked!!!")

if __name__ == "__main__":
    app = HypotenuseApp()
    app.run()