# import re
# from functools import reduce
#
# lines = 0
# words = 0
# letters = 0
#
# with open('file.txt', encoding='utf-8') as inf:  # Вариант 1
#     for line in inf:
#         lines += 1
#         reg = re.findall(r'\w+', line.rstrip())
#         words += len(reg)
#         letters += reduce(lambda x, y: x + len([i for i in y if i.isalpha()]), reg, 0)
#
# print(f"""Input file contains:
# {letters} letters
# {words} words
# {lines} lines""")


with open('files/file.txt', encoding='utf-8') as inf:  # Вариант 2
    lines, words, letters = 0, 0, 0
    for line in inf:
        lines += 1
        words += len(line.split())
        letters += sum(map(str.isalpha, line))

print(f"""Input file contains:
{letters} letters
{words} words
{lines} lines""")
