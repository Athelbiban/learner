def largest_prime_factor(numb):
    i = round(numb / 2)
     # print(i)
    while i > 1:
        for e in range(i, 1, -1):
            # print(e)
            if i % e == 0:


                # print(e)
                if numb % i == 0:
                    # print(i)
                    return i
                else:
                    pass
                pass
            pass
        i -= 1
    return False


print(largest_prime_factor(10))
# print(13195 / 2639)
