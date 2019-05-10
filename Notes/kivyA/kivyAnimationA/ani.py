from kivy.app import App
from kivy.uix.widget import Widget

class AniApp(App):
    def build(self):
        return(AniLayout())

class AniLayout(Widget):
    pass

class ClockRect(Widget):
    pass

class AniRect(Widget):
    pass


if __name__ == "__main__":
    app = AniApp()
    app.run()
