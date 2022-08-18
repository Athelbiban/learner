imt = float(input()) / float(input()) ** 2
print('Недостаточная масса' if imt < 18.5 else 'Избыточная масса' if imt > 25 else 'Оптимальная масса')
