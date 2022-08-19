def task_of_Josephus(people, retiring_numb):
    reference_point = 0
    lst = [e for e in range(1, people + 1)]

    def calculation(ret, first):
        len_lst = len(lst)
        if len_lst == 1:
            return lst[0]
        else:
            retiring = (ret % len_lst - 1 + first) % len_lst
            next_num = lst[(retiring + 1) % len_lst]
            del lst[retiring]
            first = lst.index(next_num)
        return calculation(ret, first)

    return calculation(retiring_numb, reference_point)


n, k = int(input()), int(input())

if __name__ == '__main__':
    print(task_of_Josephus(n, k))
