class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for e in self.funcs:
                if e(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i


"""
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
"""