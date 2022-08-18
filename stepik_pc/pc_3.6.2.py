import requests

with open(r'files/dataset_3378_2.txt') as inf, open(r'files/answer.txt', 'w') as ouf:
    # можно одной строкой:
    ouf.write(str(len(requests.get(inf.readline().strip()).text.splitlines())))
    # тоже самое, но для людей:
    # r = requests.get(inf.readline().strip())
    # d = r.text.splitlines()
    # ouf.write(str(len(d)))
