__author__ = 'salmon-the-wise'


def prime(n):
    i = 2
    j = 0
    while i ** 2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


a = int(input())
for i in range(a):
    x = int(input())
    print(prime(x))