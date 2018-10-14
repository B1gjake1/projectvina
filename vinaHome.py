from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.app import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
Builder.load_string("""
<HomeScreen>:
    FloatLayout:
        Button: 
            text: 'take me somewhere'
            background_color: (.96, .96, 1, 1)
            font_size: 30
            pos_hint: {'x': .25, 'center_y': .5}
            size_hint: (.5, .5)
            on_press: root.manager.current = 'settings'
            
<settingScreen>:
    # FloatLayout:
    #     slider:
    #         min: 0,
    #         max: 100,
    #         value: 50
""")


class HomeScreen(Screen):
    pass


class SettingScreen(Screen):
    pass


screens = ScreenManager()
screens.add_widget(HomeScreen(name='home'))
screens.add_widget(SettingScreen(name='settings'))


class Vina(App):
    def build(self):
        Window.clearcolor = (0, .4, .7, 1)
        return screens


if __name__ == "__main__":
    Vina().run()
