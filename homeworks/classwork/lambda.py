__author__ = 'jack-a-lynn'

# sum1 = lambda x, y: x + y
# print(sum1)
#
# numbres = input().split(" ")
# numbres = map(int, numbres)

class Map:
    def __init__(self, f, iterable):
        self.f = f
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            x = self.f(next(self.it))
        except StopIteration:
            return 15
#
# for i in Map(int, ["12", "13", "14"]):
#     print(i)


def my_map(f, iterable):
    for element in iterable:
        yield f(element)

for i in my_map(int, ["12", "13", "14"]):
    print(i)

lst = [1, 2, 3, 4, 5, 6, 7, 8]


y = list(filter(lambda x: x % 2 == 0, lst))
print(y)

numbers = list(map(input()))