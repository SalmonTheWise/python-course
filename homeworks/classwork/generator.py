__author__ = 'jack-a-lynn'
def generator_range(n):
    for i in range(n):
        yield i
x = generator_range(10)
print(type(generator_range))
print(type(x))
print(next(x))