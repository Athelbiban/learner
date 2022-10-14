def count_args(*args):
    return len(args)


print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
