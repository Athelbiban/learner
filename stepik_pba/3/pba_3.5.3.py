import requests


number = '22'
type_numb = 'math'
params = {
    'number': number,
    'type': type_numb,
}

url = f'http://numbersapi.com/{number}/{type_numb}/?json'
res = requests.get(url, params=params)
# print(res)
# print(res.headers['Content-Type'])
data = res.json()
print(('Boring', 'Interesting')[data['found']])
