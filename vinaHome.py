from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.app import Widget
class Vina(App):
    def build(self):
        Window.clearcolor = (.3, .3, .3, 1)
        root = FloatLayout(size=(500,500))
        voiceButton = Button(text="take me somewhere",
                             background_color=(0, 0, 245, 1),
                             font_size=30,
                             pos_hint={'x': .25, 'center_y': .5},
                             size_hint=(.5, .5)
                      )
        root.add_widget(voiceButton)
        return root
    pass


if __name__ == "__main__":
    Vina().run()
