# # # # years_list = [year for year in range(1985, 1990 + 1)]
# # # # print(years_list)
# # # # print(years_list[3])
# # # # print(years_list[-1])
# # #
# # # things = ["mozzarella", "cinderella", "salmonella"]
# # # print(things[1].upper())
# # # print(things)
# # # things[0] = things[0].upper()
# # # print(things)
# # # del things[2]
# # # print(things)
# #
# # surprise = ['Groucho', 'Chico', 'Harpo']
# # surprise[2] = surprise[2].lower()
# # print(surprise)
# # print(surprise[2][::-1].capitalize())
#
# even = [numb for numb in range(10) if numb % 2 == 0]
# print(even)
#
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

start1_caps = ' '.join([i.capitalize() + '!' for i in start1])
for first, second in rhymes:
    print(f'{start1_caps} {first.capitalize()}!')
    print(f'{start2} {second}.')
