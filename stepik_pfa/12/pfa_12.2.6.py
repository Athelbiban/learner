import random


def generate_ip():
    return '{}.{}.{}.{}'.format(*[random.randint(0, 255) for _ in range(4)])


if __name__ == '__main__':
    print(generate_ip())
