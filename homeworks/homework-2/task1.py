__author__ = 'salmon-the-wise'


def combinations(n, k):
    def factorial(a):
        p = 1
        for i in range(2, a + 1):
            p *= i
        return p

    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))


numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])

if 0 > n or n > 22:
    print('wrong n!')
elif k < 0:
    print('wrong k!')
else:
    print(int(combinations(n, k)))
