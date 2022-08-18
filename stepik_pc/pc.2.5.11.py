s = sorted(input().split())
sn = []
for i in range(1, len(s)):
    if s[i] == s[i - 1] and s[i] not in sn:
        sn.append(s[i])
print(' '.join(sn))
