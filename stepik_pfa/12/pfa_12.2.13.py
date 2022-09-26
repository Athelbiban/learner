import string
import random


def generate_password(length):
    password_characters = tuple((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
    return ''.join([random.choice(password_characters) for _ in range(length)])


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


if __name__ == '__main__':
    print(*generate_passwords(int(input()), int(input())), sep='\n')
