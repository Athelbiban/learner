import requests


with open('dataset_24476_3.txt') as inf:
    file = inf.read().split()
for i in file:
    type_numb = 'math'
    url = f'http://numbersapi.com/{i}/{type_numb}'
    res = requests.get(url, json=True)
    data = res.json()
    print(('Boring', 'Interesting')[data['found']])
