class UserRepository:
    def __init__(self, url, username, password):
        self.__password = password
        self.__username = username
        self.__url = url