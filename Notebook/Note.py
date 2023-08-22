import random
import datetime


class Note:
    def __init__(self):
        self.__title = None
        self.__id = "".join(str(number) for number in random.sample(range(0, 10), 4))
        self.__date = datetime.date.today().strftime("%d.%m.%y")
        self.__last_update = None
        self.__body = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_value):
        self.__title = new_value

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_value):
        self.__body = new_value

    @property
    def last_update(self):
        return self.__last_update

    @last_update.setter
    def last_update(self, new_value):
        self.__last_update = new_value

    @property
    def date(self):
        return self.__date

    @property
    def id(self):
        return self.__id
