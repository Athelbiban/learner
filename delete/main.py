import random

#string = 'abcde'
#random_index = randint(0, len(string) - 1)
#char = string[random_index]

#print(char)




# BEGIN (write your solution here)
#def choice_from_range(text, start, end):
#    return random.choice(text[start:end + 1])

# END

def choice_from_range(text, begin, end):
    return text[random.randint(begin, end)]

text = "abcdef"
#print(text[3: 5 + 1])
print(random.randint(3, 5))
print(choice_from_range(text, 3, 5))  # d
print(choice_from_range(text, 3, 5))  # f
print(choice_from_range(text, 3, 5))  # e
