for i in range(int(input())):
    lst = [int(i) for i in input().split()]
    arithmetic_mean_lst = sum(lst) / len(lst)
    counter = 0
    for e in lst:
        if e > arithmetic_mean_lst:
            counter += 1
    print(counter)
