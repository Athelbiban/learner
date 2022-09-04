def func(num1, num2):
    if num1 % num2:
        return False
    return True


print("делится" if func(int(input()), int(input())) else "не делится")
