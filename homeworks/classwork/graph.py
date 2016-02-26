

class MyDict(dict):
    # def __setitem__(self, key, value):
    #     print("MY MASTER CALLED ME")

    def __repr__(self):
        begin = "{\n"
        end = "\n}"
        to_join = ["  %s: %s" % (repr(key), repr(self[key]))
                   for key in self]
        return begin + "\n".join(to_join) + end

    def sorted_values(self):
        pairs = self.items()
        pairs = [(pair[1], pair[0]) for pair in pairs]
        pairs = sorted(pairs)
        return [pair[1] for pair in pairs]

x = MyDict()
x['a'] = 15
x['b'] = 12
x['c'] = 13
x['d'] = 27
print(sorted(x))
