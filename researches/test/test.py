import timeit
import os.path
import re


os.chdir(r'c:\Users\VostrovSO\Downloads')
directory = os.walk('main')
reg = re.compile(r'\.py$')


def f1():
    for path, dirs, files in directory:
        for file in files:
            if reg.search(file):
                break


def f2():
    for path, dirs, files in directory:
        for file in files:
            if re.search(r'\.py$', file):
                break


def f3():
    for path, dirs, files in directory:
        for file in files:
            if file.endswith('.py'):
                break


def f4():
    for path, dirs, files in directory:
        for file in files:
            if '.py' in file[-3:]:
                break


if __name__ == '__main__':
    f1 = timeit.repeat(f1)
    f2 = timeit.repeat(f2)
    f3 = timeit.repeat(f3)
    f4 = timeit.repeat(f4)

    print(f'Min time re.compile f1: {min(f1)}')
    print(f'Min time re f2:         {min(f2)}')
    print(f'Min time endswith f3:   {min(f3)}')
    print(f'Min time slice f4:      {min(f4)}')
