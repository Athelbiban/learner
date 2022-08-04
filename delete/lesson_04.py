small = False
green = False
cherry = (small, not green)
pea = (small, green)
watermelon = (not small, green)
pumpkin = (not small, not green)

if small:
    if green:
        print('pea')
    else:
        print('cherry')
else:
    if green:
        print('watermelon')
    else:
        print('pumpkin')
