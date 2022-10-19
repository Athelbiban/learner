print(all(map(lambda i: i.isdigit() and 0 <= int(i) <= 255, input().split('.'))))
