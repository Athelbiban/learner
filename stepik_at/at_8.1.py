def interpreter(string):
    a, operator, b = string.split()
    a, b = int(a), int(b)
    if operator == 'plus':
        return a + b
    elif operator == 'minus':
        return a - b
    elif operator == 'multiply':
        return a * b
    return a // b


print(interpreter(input()))
