def password_verification(password):
    upper_letter = []
    lower_letter = []
    digits = []
    for letter in password:
        if 65 <= ord(letter) <= 90:
            upper_letter.append(True)
        elif 97 <= ord(letter) <= 122:
            lower_letter.append(True)
        elif 48 <= ord(letter) <= 57:
            digits.append(True)
    return all([any(upper_letter), any(lower_letter), any(digits)])


def main(text):
    return print('YES' if all([len(text) >= 7, password_verification(text)]) else 'NO')


if __name__ == '__main__':
    main(input())
