n, z1, z2 = int(input()), complex(input()), complex(input())

print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1))
