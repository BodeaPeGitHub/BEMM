from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (300,500)

class FirstWindow(Screen):
    def afis(self):
        print('caine')

class LoginWindow(Screen):
    pass

class RegisterWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class SleepingWindow(Screen):
    pass

class SportWindow(Screen):
    pass

class WindowManager(ScreenManager):     
    pass

kv = Builder.load_file('windows.kv')

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()