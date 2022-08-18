# def is_anagram(k, m):
#     k_d = {}
#     m_d = {}
#     for i in k, m:
#         for e in i:
#             if i == k:
#                 k_d[e] = k_d.get(e, 0) + 1
#             else:
#                 m_d[e] = m_d.get(e, 0) + 1
#     return True if k_d == m_d else False
#
#
# if __name__ == '__main__':
#     print(is_anagram(input().lower(), input().lower()))


a, b = sorted(input().lower()), sorted(input().lower())
if a == b:
    print(True)
else:
    print(False)
