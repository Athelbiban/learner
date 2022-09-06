def get_count(sentence):
    sequence = 'aeiou'
    result = 0
    for i in sentence:
        if i in sequence:
            result += 1
    return result

if __name__ == '__main__':
    print(get_count('sofa'))
