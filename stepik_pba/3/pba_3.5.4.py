import requests
import json
from files.token_artsy import CLIENT_ID, CLIENT_SECRET


data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token?client_id=f408e7e0cd4db8e0a03e&client_secret=03493624e023eb8e80d892613c24514d")
r.encoding = 'utf-8'

print(r)
# разбираем ответ сервера
# j = json.loads(r.text)

# достаем токен
# token = j["token"]
# print(token)