__author__ = 'jack-a-lynn'
x = [1, 2, 3]
it = iter(x)
print(it)
print(type(it))

a = next(it)
b = next(it)
c = next(it)

print(a, b, c)

d = next(it)


class RangeIterator:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.j:
            ret_val = self.i
            self.i += 1
            return ret_val
        else:
            raise StopIteration("No more elements")


it = RangeIterator(10, 20)
for x in it:
    print(x)
