# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email
#
#
# bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
#
# print(bob.name)
# print(bob.email)


# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#
#     name = property(get_name, set_name)
#
#
# don = Duck('Donald')
# print(don.get_name())
# print(don.set_name('Stas'))
# print(don.get_name())


# class C:
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         print('getter')
#         return self._x
#
#     def setx(self, value):
#         print('setter')
#         self._x = value
#
#     def delx(self):
#         print('deletter')
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")
#
#
# c = C()
# c.x = 'Stas'


class C:
    def __init__(self):
        self._y = "Stas"

    @property
    def x(self): # В декораторах 'setter' и 'deleter' нужно указывать имя метода-свойства
        """I'm the 'x' property."""
        return self._y

    @x.setter
    def x(self, value):
        self._y = value

    @x.deleter
    def x(self):
        del self._y


c = C()
print(c.x)
c.x = 'Ivan'
print(c.x)
print(c.x)
