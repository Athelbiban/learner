import requests
import unicodedata

link = 'https://stepik.org/api/steps?ids[]=1612731'
page = requests.get(link)
js = page.json()
text = js["steps"][0]["block"]["text"]


def noneTags(string):
    flag = True
    resultString = ''
    for i in string:
        if i == '<':
            flag = False
        elif i == '>':
            flag = True
            continue
        if flag:
            resultString += i
    return resultString


s = noneTags(text).replace("\n", '')
result = s.split()[25:49]
x = list(map(lambda n: int(n[1:-1]) % 12 if n[0] == "$" else n, result))
adict = {x[i]: x[i + 1] for i in range(0, len(x), 2)}
print(adict[int(input()) % 12])
