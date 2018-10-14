from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.app import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class setting(App):
    def build(self):
        bobby = FloatLayout(size=(500, 500))
        michael = Slider(min=0,
                         max=100,
                         value=50)
        return michael

if __name__ == "__main__":
    setting().run()