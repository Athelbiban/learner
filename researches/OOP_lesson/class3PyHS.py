from datetime import datetime as dt


class Player:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, num):
        self.__lvl += Player.__type_test(num)
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__type_test(lvl)
        cls.__HEALTH = Player.__type_test(health)

    @staticmethod
    def __type_test(value):
        if isinstance(value, int):
            return value
        else:
            raise ValueError('Must be int')
