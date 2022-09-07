"""
Задача «Родословная: предки и потомки»
Условие
Даны два элемента в дереве. Определите, является ли один из них потомком другого.

Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В
каждой из следующих K строк, содержатся имена двух элементов дерева.

Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если
второй является предком первого или 0, если ни один из них не является предком другого.
"""


def pedigree_line(human):
    pedigree_list.append(human)
    if human not in pedigree_dict.keys():
        return human
    else:
        return pedigree_line(pedigree_dict[human])


pedigree_dict = {}

for i in range(int(input()) - 1):
    child, parent = input().split()
    pedigree_dict[child] = pedigree_dict.get(child, parent)

for i in range(int(input())):
    pedigree_list = []
    human_1, human_2 = input().split()
    pedigree_line(human_2)
    if human_1 in pedigree_list:
        print(1)
    else:
        pedigree_list.clear()
        pedigree_line(human_1)
        if human_2 in pedigree_list:
            print(2)
        else:
            print(0)
