# Решение задачи Эйлера №4 от zlomorda

num1 = 999
num2 = 999
polist = list()
i = 0

while num2 > 316:
    pol = num1 * num2
    pol1 = pol // 1000
    pol2 = pol % 1000
    revpol2 = int(str(pol2)[::-1])
    if pol1 == revpol2 and pol > 100000:
        polist.insert(i, pol)
        i += 1
    num1 -= 1
    if num1 < 316:
        num1 = 999
        num2 -= 1

polist.sort(reverse=True)
print(polist[0])
