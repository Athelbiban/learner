class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('Слабый пароль')

    def save(self):
        with open('users', 'a') as ouf:
            ouf.write(f'{self.login, self.password}\n')
