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
from domain.enums.ConditionEnum import Condition
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
    def logIn(self):
        global user
        username = self.ids.LoginUsername.text
        user = service.find_one_by_username(username)

class ProfileWindow(Screen):
    def on_enter(self):
        global user
        username = user.get_username()
        firstname = user.get_first_name()
        lastname = user.get_last_name()
        gender = user.get_gender()
        height = user.get_height()
        weight = user.get_weight()
        condition = user.get_condition()
        self.ids.usernameField.text = username
        self.ids.firstNameField.text = firstname
        self.ids.lastNameField.text = lastname
        self.ids.genderField.text = str(gender)
        self.ids.heightField.text = str(height)
        self.ids.weightField.text = str(weight)
        self.ids.conditionField.text = str(condition)
        

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
    global user
    def on_enter(self):
        global user
        user = service.find_one_by_username(user.get_username())
        self.ids.mainLabelNr.text = str(user.get_water_habit().get_number_of_glasses_drunk())
        self.ids.mainLabelTotal.text = str(user.get_water_habit().get_number_of_glasses())
    def addWater(self):
        global user
        user = service.find_one_by_username(user.get_username())
        glasses = int(self.ids.mainLabelNr.text)
        glasses += 1
        print("id: ", user.get_user_id(), "glasses: ", glasses)
        service.add_glasses(user.get_user_id())
        self.ids.mainLabelNr.text = str(glasses)


class SleepingWindow(Screen):
    pass

class SportWindow(Screen):
    def on_enter(self):
        global user
        workout =  user.get_sporting_habit().get_actual_workout()
        jumps = workout[0]
        squats = workout[1]
        crunches = workout[2]
        pushUps = workout[3]
        self.ids.actual_jumping_jacks.text = str(jumps)
        self.ids.actual_squats.text = str(squats)
        self.ids.actual_crunches.text = str(crunches)
        self.ids.actual_push_ups.text = str(pushUps)

        workout =  user.get_sporting_habit().get_workout()
        jumps = workout[0]
        squats = workout[1]
        crunches = workout[2]
        pushUps = workout[3]
        self.ids.to_do_jumping_jacks.text = str(jumps)
        self.ids.to_do_squats.text = str(squats)
        self.ids.to_do_crunches.text = str(crunches)
        self.ids.to_do_push_ups.text = str(pushUps)


class RunWindow(Screen):
    pass

class WindowManager(ScreenManager):     
    pass


kv = Builder.load_file('gui/windows.kv')

class MyApp(App):
    def build(self):
        return kv
