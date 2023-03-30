from class1 import Verification


class V2(Verification):
    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users') as ouf:
            for i in ouf:
                if f'{self.login, self.password}\n' == i:
                    raise ValueError(f'Пользователь {self.login} с таким паролем уже есть')
        super().save()

    def show(self):
        return self.login, self.password


y = V2('Stas', '112233445', 37)
