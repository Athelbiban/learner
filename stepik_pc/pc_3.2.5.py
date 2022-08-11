def update_dictionary(d, key, value):
    if key in d:
        d[key] = d.get(key) + [value]
    elif key * 2 in d:
        d[key * 2] = d.get(key * 2) + [value]
    else:
        d[key * 2] = d.get(key, [value])


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
