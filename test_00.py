cords = list(map(str,[111,211,311,121,221,321,131,231,331,112,212,312,122,222,322,132,232,332,113,213,313,123,223,323,133,233,333]))
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
dic = {a:c for a,c in zip(alpha, cords)}
print(cords)
print(dic)
print(alpha[25])
