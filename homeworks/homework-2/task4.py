a, *args = (int(i) for i in input().split())

def rpfilter(a, *args):
    def euclid(n, m):
        while n != 0 and m != 0:
            if n >= m:
                if n % m == 0:
                    return m
                else:
                    return euclid(m, n % m)
            else:
                if m % n == 0:
                    return n
                else:
                    return euclid(n, m % n)


    list_args = str()
    for arg in args:
        if euclid(a, arg) == 1:
            list_args += str(arg) + " "
    if len(list_args) == 0:
        return None
    return list_args

print (rpfilter(a, *args))