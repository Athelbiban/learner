class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity - self.count - v >= 0

    def add(self, v):
        if self.can_add(v):
            self.count += v


x = MoneyBox(12)
print(x.capacity)
print(x.count)
print(x.can_add(13))
