import requests
import time
from files.token_artsy import CLIENT_ID, CLIENT_SECRET


data = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
r = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=data).json()
headers = {'X-Xapp-Token': r['token']}

with open('files/dataset_24476_4.txt', encoding='utf-8') as inf,\
        open('files/answer.txt', 'w', encoding='utf-8') as ouf:
    lst = []
    for author_id in inf:
        time.sleep(1)
        author_id = author_id.rstrip()
        req = requests.get(f"https://api.artsy.net/api/artists/{author_id}", headers=headers).json()
        author_name = req['sortable_name']
        author_birthday = req['birthday']
        lst.append((author_name, author_birthday))
    for name, _ in sorted(lst, key=lambda x: (x[1], x[0])):
        ouf.write(f'{name}\n')
