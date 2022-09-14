import re

res = re.sub(r'[-.,;:?!]', '', input().lower())
print(len(set(res.split())))

# res = [i.strip('-.,;:?!').lower() for i in input().split()]
# print(len(set(res)))
