### Мой вариант.
import re


def split_encode_series(string):
    return [(len(i[0]), i[1]) for i in re.finditer(r'(\w)\1*', string)]


def encode_series(series):
    result = ''
    for i, e in series:
        if i == 1:
            result += e
        else:
            result += str(i) + e
    return result


def rle_encode(string):
    return encode_series(split_encode_series(string))


print(rle_encode('aaabccccCCaB'))


### Вариант товарища из комментов к задаче:

# import re
#
#
# def split_encode_series(string):
#     i = re.findall(r"((\w)\2*)", string)
#     return ((len(a), e) for a, e in i)
#
#
# def encode_series(series):
#     return (str(i[0]) + str(i[1]) if i[0] > 1 else i[1] for i in series)
#
#
# def rle_encode(string):
#     return ''.join(encode_series(split_encode_series(string)))
#
#
# print(rle_encode('aaabccccCCaB'))
