def code(string, shift):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    code_string = ''
    for i in string:
        code_string += alphabet[(alphabet.index(i) + shift) % len(alphabet)]
    return f'Result: "{code_string}"'


shift_code, string_code = int(input()), input().strip()

print(code(string_code, shift_code))
