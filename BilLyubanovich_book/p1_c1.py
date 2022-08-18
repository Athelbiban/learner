import re

song = """When an eel grabs your arm,
Ahn it causes great harm,
That's - a moray!"""
print(song)
reg = re.findall(r'\b[m]\w*', song)
print(song.replace(reg[0], reg[0].capitalize()))
