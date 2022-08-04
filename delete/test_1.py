def sort_pair(couple):
    (a, b) = couple
    #print(couple)
    #print((a, b))
    #print(a)
    #print(b)
    if a <= b:
        # print((a, b))
        couple = (a, b)
        #print(couple)
        return couple
    else:
        # print((b, a))
        couple = (b, a)
        #print(couple)
        return couple


print(sort_pair((5, 1)))
print(sort_pair((2, 2)))
print(sort_pair((7, 8)))
