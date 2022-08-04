lst_in = input().split('_')
lst_out = []
for word in lst_in:
    lst_out.append(word.capitalize())
print(''.join(lst_out))

# str_in = ' '.join(input().split('_')).title()
# print(str_in.replace(' ', ''))
