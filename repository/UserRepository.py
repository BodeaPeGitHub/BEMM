class UserRepository:

    def __init__(self, url, username, password):
        self.__password = password
        self.__username = username
        self.__url = url

    def save(self, user):
        pass

    def update(self, user):
        pass

    def delete(self, user):
        pass

    def find_one(self, username):
        pass

    def find_all(self):
        pass

