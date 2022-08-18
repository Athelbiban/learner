def modify_list(a):
    a[:] = [i // 2 for i in a if not i % 2]


lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
