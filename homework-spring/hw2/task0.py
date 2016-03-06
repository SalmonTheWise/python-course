ancestors = []

if issubclass(D, A):
    ancestors.append("A")
if issubclass(D, B):
    ancestors.append("B")
if issubclass(D, C):
    ancestors.append("C")

ancestors.sort()
print(" ".join(ancestors))
