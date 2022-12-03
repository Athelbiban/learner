import random
import string


def generate_password(length):
    password = []
    # password.extend(random.choice(char) for char in (low, up, dig))
    password.extend(random.choice(all_char) for _ in range(length))
    random.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


if __name__ == '__main__':
    low = tuple(set(string.ascii_lowercase) - set('lo'))
    up = tuple(set(string.ascii_uppercase) - set('IO'))
    dig = tuple(string.digits)
    # signs_full = tuple("!#$%&'()*+,-./:;<=>?@[]^_`{|}~\"")
    signs_cut = tuple("!,-.:;?_")
    low_up_dig = low + up + dig
    all_char = low + up + dig + signs_cut
    print(*generate_passwords(int(input('Сколько паролей генерировать: ')),
                              int(input('Количество символов в пароле: '))), sep='\n')
