class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for v in a:
            if len(self.lst) < 5:
                self.lst.append(v)
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst.clear()

    def get_current_part(self):
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())  # вернуть [1]
buf.add(1, 3)  # Ничего не выводит
print(buf.get_current_part())  # вернуть [1, 1, 3]
buf.add(2, 4)  # Вывод print(11)
print(buf.get_current_part())  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1)  # Вывод print(5)
print(buf.get_current_part())  # вернуть [1, 1, 1]
