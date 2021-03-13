from singleton import Singleton


class DatabaseConnection(Singleton):
    pass


print(id(DatabaseConnection()) == id(DatabaseConnection()))
