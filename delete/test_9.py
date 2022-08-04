import re


def inputs():
    global line
    while True:
        try:
            line = input()
            yield line
        except (ValueError, EOFError):
            if re.findall(reg1, line, flags=re.MULTILINE):
                print('Private')
            elif re.findall(reg2, line, flags=re.MULTILINE):
                print('Taxi')
            else:
                print('Fail')


reg1 = "^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{3}"
reg2 = "[АВЕКМНОРСТУХ]{2}\d{5}"

inputs()
