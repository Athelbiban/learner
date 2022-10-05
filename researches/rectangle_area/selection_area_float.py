import numpy as np

d = 43
for x in np.arange(0.1, d, 0.1):
    for y in np.arange(0.1, d, 0.1):
        if round(x, 2) * round(y, 2) == 12:
            for z in np.arange(0.1, d, 0.1):
                if round(z, 2) * round(y, 2) == 24:
                    for n in np.arange(0.1, d, 0.1):
                        for q in np.arange(0.1, d, 0.1):
                            if round(n, 2) > round(q, 2) and round(n, 2) + round(q, 2) == round(z, 2):
                                for s in np.arange(0.1, d, 0.1):
                                    if round(s, 2) * round(q, 2) == 9 and round(x, 2) * round(s, 2) == 18:
                                        for a in np.arange(0.1, d, 0.1):
                                            if (round(s, 2) + round(a, 2)) * round(n, 2) == 42:
                                                for b in np.arange(0.1, d, 0.1):
                                                    if round(b, 2) - round(q, 2) == round(x, 2):
                                                        print(f'a:{round(a, 2)}', f'b:{round(b, 2)}',
                                                              f'S:{(round(a, 2) * round(b, 2))}')
