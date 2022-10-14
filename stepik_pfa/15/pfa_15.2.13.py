def greet(name, *args):
    # s = f'Hello, {name}'  # Вариант 1
    # for i in args:
    #     s += f' and {i}'
    # return s + '!'
    return f'Hello, {" and ".join((name,) + args)}!'  # Вариант 2


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
