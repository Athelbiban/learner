import re


def pig_it(text):
    # words = re.findall(f'\w+', text)  # Вариатн 1
    # for word in words:
    #     text = re.sub(f'\\b{word}', f'{word[1:]}{word[0]}ay', text)
    # return text

    return re.sub(r'(\w)(\w*)', r'\2\1ay', text)  # Вариатн 2

    # return __import__("re").sub(r'\b\w+\b', lambda a: a.group(0)[1:] + a.group(0)[0] + 'ay', text)  # Вариант 3


if __name__ == '__main__':
    print(pig_it('This is my, a string! !'))
