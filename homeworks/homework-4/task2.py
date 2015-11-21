inp = open("dict.txt", "r")
noun = 0
adj = 0
verb = 0
for line in inp:
    for word in line.split('\n'):
        if word[(len(word) - 2):len(word)] == "ka":
            noun += 1
        elif word[(len(word) - 2):len(word)] == "yo":
            adj += 1
        else:
            verb += 1
inp.close()

import math

if adj < 7:
    n = adj
else:
    n = 7
adj_comb = 0
for i in range(n):
    adj_comb += math.factorial(adj)/(math.factorial(adj-(i+1)))

cool_comb = adj_comb * noun * verb
print(int(cool_comb))


