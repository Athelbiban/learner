numb, lst = int(input()), []
for i in range(1, numb + 1):
    counter = 0
    while counter < i and len(lst) < numb:
        lst.append(i)
        counter += 1
print(*lst)
