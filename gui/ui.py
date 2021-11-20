from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from domain.User import User

Window.size = (300,500)
user = "caine"

class FirstWindow(Screen):
    def afis(self):
        print('caine')

class LoginWindow(Screen):
    pass

class ProfileWindow(Screen):
    pass

class RegisterWindow(Screen):
    def register(self):
        # username = str(self.ids['username'].text)
        # firstname = str(self.ids[firstname].text)
        # lastname = str(self.ids.lastname.text)
        # print(username)
        print(self.ids)


class MainWindow(Screen):
    pass


class SleepingWindow(Screen):
    pass

class SportWindow(Screen):
    pass

class RunWindow(Screen):
    pass

class WindowManager(ScreenManager):     
    pass


kv = Builder.load_file('gui/windows.kv')

class MyApp(App):
    def build(self):
        return kv
