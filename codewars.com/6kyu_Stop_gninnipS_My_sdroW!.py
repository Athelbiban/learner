# def spin_words(sentence):
#     lst = []
#     for i in sentence.split():
#         if len(i) >= 5:
#             i = i[::-1]
#         lst.append(i)
#     return ' '.join(lst)
#
#
# if __name__ == '__main__':
#     print(spin_words("Hey fellow warriors"))


# Лучший вариант в комментах:
def spin_words(sentence):
    return " ".join(x[::-1] if len(x) >= 5 else x for x in sentence.split(" "))


if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))
