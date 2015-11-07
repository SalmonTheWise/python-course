__author__ = 'jack-a-lynn'

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

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(2, 1000):
        if prime(i):
            print(i)

#print("I'M SO AWESOME, I KNOW HOW MODULES WORK")
