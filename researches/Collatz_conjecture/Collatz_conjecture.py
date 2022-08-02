import time

start = time.time()


def collatz_conjecture(n):
    lst = [n]
    while n > 1:
        n = n * 3 + 1 if n % 2 else n // 2
        lst.append(n)
    return lst


def sequence_1(n):
    seq_1 = {}
    for i in range(n + 1):
        a = collatz_conjecture(i)
        seq_1[i] = seq_1.get(i, a)
    return seq_1


def sequence_2(n):
    s = sequence_1(n)
    seq_2 = {}
    for i in s:
        seq_2[i] = seq_2.get(i, (len(s.get(i)), max(s.get(i))))
    return seq_2


def main(num):
    s = sequence_2(num)
    sort_max_value = sorted(s.items(), key=lambda x: x[1][1], reverse=True)
    sort_max_length = sorted(s.items(), key=lambda x: x[1][0], reverse=True)
    t = [sort_max_value[0]]
    y = [sort_max_length[0]]
    ln = sum(e[0] for i, e in sort_max_length) / len(sort_max_length)
    for i in range(1, len(sort_max_value) + 1):
        if t[0][1][1] <= sort_max_value[i][1][1]:
            t.append(sort_max_value[i])
        else:
            break
    for i in range(1, len(sort_max_length) + 1):
        if y[0][1][0] <= sort_max_length[i][1][0]:
            y.append(sort_max_length[i])
        else:
            break
    return t, y, ln


if __name__ == '__main__':
    m_val, m_len, av_ln = main(1_000_000)
    print('Макс. значение:', m_val[0][1][1])
    print('Количество макс. значений:', len(m_val), '\nЧисла:', *(i for i, e in m_val))
    print('Макс. длина:', m_len[0][1][0])
    print('Количество макс. длин последовательностей:', len(m_len), '\nЧисла:', *(i for i, e in m_len))
    print('Средняя длина последовательностей:', f'{av_ln:.2f}')

print(time.time() - start)
