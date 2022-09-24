from string import ascii_uppercase as u
from random import choice as c, randrange as r


def generate_index():
    return f'{c(u)}{c(u)}{r(100)}_{r(100)}{c(u)}{c(u)}'


if __name__ == '__main__':
    print(generate_index())
