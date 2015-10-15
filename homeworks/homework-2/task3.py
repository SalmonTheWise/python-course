numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])


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


print(euclid(n, m))
