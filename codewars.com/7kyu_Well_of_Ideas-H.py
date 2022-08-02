# def well(arr):
#     counter = 0
#     for i in arr:
#         for e in i:
#             if str(e).lower() == 'good':
#                 counter += 1
#     if 1 <= counter <= 2:
#         return 'Publish!'
#     elif counter > 2:
#         return 'I smell a series!'
#     return 'Fail!'
#
#
a = [['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]
#
# if __name__ == '__main__':
#     print(well(a))

print(str(a).lower().count('good'), a, sep='\n')
