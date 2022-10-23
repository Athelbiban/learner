import random as rnd

with open('files/first_names.txt', encoding='utf-8') as inf1, open('files/last_names.txt', encoding='utf-8') as inf2:
    first_names_list = list(inf1)
    last_names_list = list(inf2)
    for _ in '...':
        print(rnd.choice(first_names_list).rstrip(), rnd.choice(last_names_list).rstrip())
