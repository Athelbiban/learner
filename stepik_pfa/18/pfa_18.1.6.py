"""
Forbidden words 🌶️
На вход программе подается строка текста с именем текстового файла. Напишите программу,
выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов
звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
Гарантируется, что все слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором
необходимо заменить запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались,
даже если они встречаются в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например,
если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM,
EXAM и подобные должны быть заменены на ****.

Примечание 3. Если бы файл forbidden_words.txt содержал слова:

hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
то результатом будет:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
"""


with open('files/forbidden_words.txt', encoding='utf-8') as inf1, open(f'files/data.txt', encoding='utf-8') as inf2:
    text = []
    forbidden_list = inf1.read().split()
    for word in inf2.read().split(' '):
        word_lower = word.lower()
        for xxx in forbidden_list:
            if xxx in word_lower:
                start = word_lower.index(xxx)
                stop = start + len(xxx)
                new_word = word[:start] + '*'*len(xxx) + word[stop:]
                word = new_word
        text.append(word)

print(*text)
