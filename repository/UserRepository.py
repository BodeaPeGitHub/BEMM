from datetime import datetime

import pyodbc

from domain.User import User


class UserRepository:

    def __init__(self, server_name, db_name):
        self.__db_name = db_name
        self.__server_name = server_name
        self.__con_srt = ("Driver={SQL Server Native Client 11.0};"
                          "Server=" + str(self.__server_name) + ";"
                                                                "Database=" + str(self.__db_name) + ";"
                                                                                                    "Trusted_Connection=yes;")

    def save(self, user):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        my_date = user.get_birthday()
        my_datetime = datetime(my_date.year, my_date.month, my_date.day).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f"insert into Users(username, first_name, last_name, gender, height, weight, minutes_run, sleeping_time, glasses_drank, jumping_jacks, squats, crunches, push_ups, birthday) values ('{user.get_username()}', '{user.get_first_name()}', '{user.get_last_name()}', '{user.get_gender()}', '{user.get_height()}', '{user.get_weight()}', '0', '0', '0', '0', '0', '0', '0', '{my_datetime}')")
        cursor.commit()

    def update(self, user):
        jumping_jacks, squats, crunches, push_ups = user.get_sporting_habit().get_actual_workout()
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        cursor.execute(f"update Users set minutes_run={user.get_running_habit().get_minutes_ran()}, sleeping_time={user.get_sleeping_habit().get_hours_slept()}, glasses_drank={user.get_water_habit().get_number_of_glasses_drunk()}, jumping_jacks={jumping_jacks}, squats={squats}, crunches={crunches}, push_ups={push_ups} where id={user.get_user_id()}")
        cursor.commit()

    def update_attribute(self, attribute, value, user_id):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        cursor.execute(f"update Users set {attribute} = {value} where id = {user_id}")

    def delete(self, user_id):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        cursor.execute(f"delete from Users where id={user_id}")
        cursor.commit()

    def find_one(self, user_id):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        user = cursor.execute(f"select * from Users where id={user_id}").fetchall()
        return self.__extract_user(user[0])

    def __extract_user(self, item):
        username = item.__getitem__(0)
        first_name = item.__getitem__(1)
        last_name = item.__getitem__(2)
        user_id = item.__getitem__(3)
        gender = item.__getitem__(4)
        height = item.__getitem__(5)
        birthday = item.__getitem__(6)
        weight = item.__getitem__(7)
        minutes_ran = item.__getitem__(8)
        sleeping_time = item.__getitem__(9)
        glasses_drank = item.__getitem__(10)
        jumping_jacks = item.__getitem__(11)
        squats = item.__getitem__(12)
        crunches = item.__getitem__(13)
        push_ups = item.__getitem__(14)
        user = User(username, first_name, last_name, gender, birthday, weight, height)
        user.set_user_id(user_id)
        user.get_running_habit().set_minutes_ran(minutes_ran)
        user.get_sleeping_habit().set_number_hour_slept(sleeping_time)
        user.get_water_habit().set_glass_of_water_drunk(glasses_drank)
        sporting = user.get_sporting_habit()
        sporting.set_jumping_jacks(jumping_jacks)
        sporting.set_squats(squats)
        sporting.set_crunches(crunches)
        sporting.set_push_ups(push_ups)
        return user

    def find_all(self):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        users = cursor.execute("select * from Users")
        all_user = []
        for almost_user in users:
            all_user.append(self.__extract_user(almost_user))
        return all_user

    def find_one_by_username(self, username):
        conn = pyodbc.connect(self.__con_srt)
        cursor = conn.cursor()
        user = cursor.execute(f"select * from Users where username='{username}'").fetchall()
        return self.__extract_user(user[0])