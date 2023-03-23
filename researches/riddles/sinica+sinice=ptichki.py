for e in range(100_000, 1_000_000):
    i = e // 2
    if i + i == e and len(str(i)) == 6 and\
            e % 10 == i // 100 % 10 == i // 10_000 % 10 == e // 1000 % 10 and \
            str(i)[0] not in str(i)[1:] and \
            str(i)[2] not in str(i)[:2] and str(i)[2] not in str(i)[3:] and \
            str(i)[2] not in str(i)[:2] and str(i)[2] not in str(i)[3:] and \
            str(i)[-2] not in str(i)[:-2] and str(i)[-2] != str(i)[-1] and \
            str(i)[-1] not in str(i)[:-1] and \
            str(e)[0] not in str(i) and \
            str(e)[1] not in str(i) and \
            str(e)[3] not in str(i) and \
            str(e)[4] not in str(i):
        print(f'птички: {e}', f'синица: {i}')
