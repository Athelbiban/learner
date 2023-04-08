import requests
import re


def find_url(A, B, count=0):
    res = requests.get(A).text.replace('stepic.org', 'stepik.org')
    list_url = re.findall(r'<a href="(.+)">', res)
    if count == 1:
        if B in list_url:
            return True
        return False
    for C in list_url:
        if find_url(C, B, count + 1):
            return 'Yes'
    return 'No'


print(find_url(input().replace('stepic.org', 'stepik.org'), input().replace('stepic.org', 'stepik.org')))
