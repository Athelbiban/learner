print(*sorted(input().split(), key=lambda string: sum(map(int, string))))
