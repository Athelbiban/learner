import requests

with open(r'files/dataset_3378_3.txt') as inf, open(r'files/answer.txt', 'w') as ouf:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/'
    r = requests.get(inf.readline().strip()).text
    while r[:2] != 'We':
        r = requests.get(url + r).text
        print(r) # чтобы не паниковать, пока работает скрипт
    ouf.write(r)
