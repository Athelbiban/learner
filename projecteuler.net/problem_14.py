"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это
до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все
сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.

P.S. Задача решена 2.08.22г. (/researches/Collatz_conjecture/Collatz_conjecture.py)
в рамках самостоятельного исследования последовательности Коллатца, в следствие решения
какой-то задачи на данную тематику из курса Stepik "Адаптивный тренажер Python".
"""


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
