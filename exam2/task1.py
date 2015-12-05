import re

inp = open("hp5.txt", "r")
out = open('answer.txt', 'w')
text = inp.read().replace("\n", " ")


list_2 = re.findall('([A-Z]\w+ [A-Z]\w+|[A-Z]\w+) whispered', text)
list_3 = re.findall('whispered ([A-Z]\w+ [A-Z]\w+|[A-Z]\w+)', text)


print(list_2)
print(list_3)
