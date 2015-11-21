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
cool_comb = ((1, 2, 3, 4, 5, 6, 7,) ** adj)*noun*verb
print(cool_comb)


