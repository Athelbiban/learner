shift, original_s, code_s = int(input()), input(), []
start, end = int('1F600', 16), int('1F64F', 16)
for i in range(len(original_s)):
    if ord(original_s[i]) + shift < end:
        code_s.append(chr((ord(original_s[i]) + shift) % end))
    else:
        code_s.append(chr((ord(original_s[i]) + shift) % end + start))
s = ''.join(str(i) for i in code_s)
print(f'Result: "{s}"')
