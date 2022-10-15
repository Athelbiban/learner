def print_products(*args):
    [print(f'{num + 1}) {prod}') for num, prod in enumerate(i for i in args if isinstance(i, str) and i)] \
        or [print('Нет продуктов')]


if __name__ == '__main__':
    print_products('Рис', '', 'Гречка', ['Булгур'], True, 12, 3.1415, {1, 2, 3}, {1: 4, 2: 3}, 'Салфетки', 'Сыр', 'Горчица', 12, '', 'Чайник')
