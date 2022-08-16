def encode_decode(encode, decode, key):
    en_str, de_str = '', ''
    for later in encode:
        en_str += key[later]
    key = {i: e for e, i in key.items()}
    for later in decode:
        de_str += key[later]
    return en_str, de_str


def main(encode, decode, key):
    print(*encode_decode(encode, decode, key), sep='\n')


key_dict = {i: e for i, e in zip(input(), input())}
encode_str, decode_str = input(), input()

if __name__ == '__main__':
    main(encode_str, decode_str, key_dict)
