d = {}
for _ in range(int(input())):
    numb, name = input().split()
    d[numb] = name.upper()

for _ in range(int(input())):
    f_name = input().upper()
    flag = 'абонент не найден'
    for k, v in d.items():
        if f_name == v:
            print(k, end=' ')
            flag = ''
    print(flag)
