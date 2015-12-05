import re

inp = open("hp5.txt", "r")
out = open('answer.txt', 'w')
text = inp.read().replace("\n", " ")


list_2 = re.findall('([A-Z]\w+ [A-Z]\w+|[A-Z]\w+) whispered', text)
list_3 = re.findall('whispered ([A-Z]\w+ [A-Z]\w+|[A-Z]\w+)', text)

all = []
for i in range(len(list_3)):
    all.append(list_3[i])
for i in range(len(list_2)):
    all.append(list_2[i])

def f(lst):
    elems = {}
    e, em = None, 0
    for i in lst:
        elems[i] = t = elems.get(i, 0) + 1
        if t > em:
            e, em = i, t
    return em, e

l = f(all)
print(' '.join([str(x) for x in l]))
