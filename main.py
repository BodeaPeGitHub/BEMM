
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date
from gui.ui import MyApp
import datetime
from domain.User import User
from repository.UserRepository import UserRepository


def test_db():
    repo = UserRepository("localhost", "BEMM")
    user = User("Matei21", "Matei", "Birjovanu", "M", datetime.date(2001, 2, 21), 63, 90)
    user.set_user_id(35)
    repo.save(user)
    # repo.update(user)
    # repo.delete(34)
    for user in repo.find_all():
        print(user)
    #repo.find_one("Mara")


if __name__ == '__main__':
    #test_db()
    #print('Totul merge ca pe roate.')
    ui = MyApp()
    ui.run()
    
