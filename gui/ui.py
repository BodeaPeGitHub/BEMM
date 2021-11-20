from datetime import datetime
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
from controller.UserService import UserService
from repository.UserRepository import UserRepository
from domain.validator.UserValidator import UserValidator
from datetime import date

Window.size = (300,500)
user = "caine"
validator = UserValidator()
repository = UserRepository("localhost", "BEMM")
service = UserService(repository,validator)

class FirstWindow(Screen):
    def afis(self):
        print('caine')

class LoginWindow(Screen):
    pass

class ProfileWindow(Screen):
    pass

class RegisterWindow(Screen):
    def register(self):
        global user
        username = str(self.ids.username.text)
        firstname = str(self.ids.firstname.text)
        lastname = str(self.ids.lastname.text)
        print(username,firstname,lastname)
        user = User(username,firstname,lastname,"F",date.today(),50,210)
        service.save(username,firstname,lastname,"F",date.today(),50,210)


class MainWindow(Screen):
    def addWater(self):
        global user
        user = service.find_one_by_username(user.get_username())
        glasses = int(self.ids.mainLabelNr.text)
        glasses+=1
        print("id: ",user.get_user_id(),"glasses: ",glasses)
        service.add_glasses(user.get_user_id())
        self.ids.mainLabelNr.text = str(glasses)


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
