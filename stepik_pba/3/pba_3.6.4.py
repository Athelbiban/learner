import xml.etree.ElementTree as ET


def f(r, count=1):
    d[r.attrib['color']] += count
    for i in r:
        f(i, count + 1)


example_xml = input().rstrip()
root = ET.fromstring(example_xml)
d = {'red': 0, 'green': 0, 'blue': 0}
f(root)
print(d['red'], d['green'], d['blue'])
