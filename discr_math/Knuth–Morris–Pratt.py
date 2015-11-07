def kmp(a, b):
    index = -1
    for i in xrange(len(a) - len(b)+1):
        success = True
        for j in xrange(len(b)):
            if b[j] <> a[i+j]:
                success = False
                break
        if success:
            index = i
            break
    return index