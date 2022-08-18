# # Мой вариант первым способом (исправленный по варианту со stepik):
# start, end = int('1f600', 16), int('1f64f', 16)
# s, t, res = int(input()), input(), []
# for i in range(len(t)):
#     res.append(chr((ord(t[i]) + s - end - 1) % (end - start + 1) + start))
# print(f'Result: "{"".join(i for i in res)}"')

# Мой правильный вариант, но вторым способом:
alphabet = [chr(i) for i in range(int('1f600', 16), int('1f64f', 16) + 1)]
shift, orig_str, result = int(input()), input(), []

for i in orig_str:
    result.append(alphabet[(alphabet.index(i) + shift) % len(alphabet)])
print(f'Result: "{"".join(i for i in result)}"')


## Один из вариантов со stepik, как у меня способ №1, но вроде правильный:
# shift = int(input())
# res = []
# for i in input():
#     res.append(chr((ord(i) + shift - 128592) % 80 + 128512))
# res1 = ''.join(res)
# print(f'Result: "{res1}"')
