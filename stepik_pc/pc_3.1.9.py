def modify_list(a):
    for i, e in enumerate(a):
        if e % 2:
            a[i] = 'odd'
    while 'odd' in a:
        a.remove('odd')
    for k, m in enumerate(a):
        a[k] = m // 2


lst = [10, 5, 8, 3, 0]
modify_list(lst)
print(lst)
