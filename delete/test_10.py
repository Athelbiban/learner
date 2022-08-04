import re

#получаем серии (в виде списка кортежей)
series = re.findall(r'((\w)\2*)', 'aaabccccCCaB')
print(series)
#формируем строку, удаляя длины, равные 1
print(''.join([re.sub(r'\b1\b', '',str(len(crt[0])))+crt[1] for crt in series]))
