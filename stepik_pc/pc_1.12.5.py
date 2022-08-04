a, b, c = int(input()), int(input()), int(input())
max_numb = 0
min_numb = 0
med_numb = 0

if a >= b >= c:
    max_numb = a
    med_numb = b
    min_numb = c
elif a >= c >= b:
    max_numb = a
    med_numb = c
    min_numb = b
elif b >= c >= a:
    max_numb = b
    med_numb = c
    min_numb = a
elif b >= a >= c:
    max_numb = b
    med_numb = a
    min_numb = c
elif c >= a >= b:
    max_numb = c
    med_numb = a
    min_numb = b
else:
    max_numb = c
    med_numb = b
    min_numb = a

print(max_numb, min_numb, med_numb, sep='\n')
