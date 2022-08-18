card1, card2 = input().split()
d = ['6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']
trump = input()

if card1[-1] == card2[-1]:
    if d.index(card1[0]) > d.index(card2[0]):
        print('First')
    elif d.index(card1[0]) < d.index(card2[0]):
        print('Second')
    else:
        print('Error')
else:
    if card1[-1] == trump:
        print('First')
    elif card2[-1] == trump:
        print('Second')
    else:
        print('Error')
