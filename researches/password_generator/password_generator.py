import string
from secrets import SystemRandom


def generate_password(length, char):
    crypto = SystemRandom()
    password = []
    # password.extend(crypto.choice(char) for char in (low, up, dig))
    password.extend(crypto.choice(char) for _ in range(length))
    crypto.shuffle(password)
    return ''.join(password)


def generate_passwords(count, length, char):
    return [generate_password(length, char) for _ in range(count)]


def main():
    low = tuple(set(string.ascii_lowercase) - set('lo'))
    up = tuple(set(string.ascii_uppercase) - set('IO'))
    dig = tuple(string.digits)
    # signs_full = tuple("!#$%&'()*+,-./:;<=>?@[]^_`{|}~\"")
    signs_cut = tuple("!,-.:;?_")
    # low_up_dig = low + up + dig
    all_char = low + up + dig + signs_cut
    print(*generate_passwords(int(input('Сколько паролей генерировать: ')),
                              int(input('Количество символов в пароле: ')),
                              all_char), sep='\n')


if __name__ == '__main__':
    main()
