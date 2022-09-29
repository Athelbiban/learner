numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j,
           3 - 2j, -9 + 9j,-1 - 1j, -1 - 10j, -20 + 15j,
           -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
abs_numbers = [abs(i) for i in numbers]

print(numbers[abs_numbers.index(max(abs_numbers))], max(abs_numbers), sep='\n')
