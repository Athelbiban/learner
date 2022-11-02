import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, elem):
        super().append(elem)
        self.log(elem)


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
