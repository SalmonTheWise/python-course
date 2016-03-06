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

m = int(input())
excs = []
for k in range(m):
    exc = input()
    excs.append(exc)


cnt = 0
for e in excs:
    visited = []
    chk(e)
    for j in visited:
        if j in excs[:cnt]:
            print(e)
            break
    cnt += 1
