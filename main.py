import datetime

from domain.User import User
from repository.UserRepository import UserRepository


def test_db():
    repo = UserRepository("localhost\SQLEXPRESS", "BEMM")
    user = User("Matei21", "Matei", "Birjovanu", "M", datetime.date(2001, 2, 21), 63, 90)
    user.set_user_id(35)
    user.get_running_habit().set_minutes_ran(2)
    user.get_sleeping_habit().set_number_hour_slept(3)
    user.get_water_habit().set_glass_of_water_drunk(4)
    sporting = user.get_sporting_habit()
    sporting.set_jumping_jacks(5)
    sporting.set_squats(6)
    sporting.set_crunches(7)
    sporting.set_push_ups(8)
    repo.update(user)
    repo.delete(34)
    for user in repo.find_all():
        print(user)
    repo.find_one("Mara")


if __name__ == '__main__':
    test_db()
    print('Totul merge ca pe roate.')
