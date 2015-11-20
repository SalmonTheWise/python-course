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
cool_comb = (1 ** adj + 2 ** adj + 3 ** adj + 4 ** adj + 5 ** adj + 6 ** adj + 7 ** adj)*noun*verb
print(cool_comb)


