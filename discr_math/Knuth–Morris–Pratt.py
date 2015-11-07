def kmp(a, b):
    index = -1
    for i in range(len(a) - len(b)+1):
        success = True
        for j in range(len(b)):
            if b[j] != a[i+j]:
                success = False
                break
        if success:
            index = i
            break
    return index
