def likes(names):
    len_names = len(names)
    str_names = 'no one likes this'
    if len_names == 1:
        str_names = f'{names[0]} likes this'
    elif len_names == 2:
        str_names = f'{names[0]} and {names[1]} like this'
    elif len_names == 3:
        str_names = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len_names > 3:
        str_names = f'{names[0]}, {names[1]} and {len_names - 2} others like this'
    return str_names


# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
