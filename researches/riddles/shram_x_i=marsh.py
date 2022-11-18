for e in range(1_000, 10_000):
    for i in range(2, 10):
        k = int(str(e)[::-1])
        if e * i == k:
            print(f'шрам: {e}', f'ы: {i}', f'марш: {k}')
