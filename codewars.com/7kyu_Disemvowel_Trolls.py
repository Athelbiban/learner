def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in string_:
        if letter in vowels:
            continue
        else:
            result += letter
    return result


if __name__ == '__main__':
    print(disemvowel('Process finished with exit code 0!!!'))
