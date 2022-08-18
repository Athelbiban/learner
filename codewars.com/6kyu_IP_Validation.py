def is_valid_IP(strng):
    lst = strng.split('.')
    if len(lst) != 4:
        return False
    for i in lst:
        if not i.isdigit() or len(i) > 1 and int(i[0]) == 0 or int(i) > 255:
            return False
    return True


if __name__ == '__main__':
    print(is_valid_IP('254..127.215'))
