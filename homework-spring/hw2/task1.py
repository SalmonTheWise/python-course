n = int(input())

cls = {}
for i in range(n):
    desc, *anc = input().split(" : ")
    if anc:
        anc = anc[0].split(" ")
    if desc not in cls:
        cls[desc] = anc
    else:
        cls[desc].append(anc)


def chk(x):
    if x not in visited:
        visited.append(x)
        if x in cls:
            for l in cls[x]:
                chk(l)
    else:
        return

q = int(input())
pairs = []
for k in range(q):
    pairs.append(input())


for pair in pairs:
    visited = []
    ancest, descend = pair.split(' ')
    chk(descend)
    if descend == ancest or ancest in visited:
        print('Yes')
    else:
        print('No')





