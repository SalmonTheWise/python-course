class fibonacci_sequence:
    def __init__(self, n):
        self.n = n
        self.a = 1
        self.b = 1
        self.el = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.el < self.n:
            ret_val = self.a
            self.a, self.b = self.b, self.b + ret_val
            self.el += 1
            return ret_val
        else:
            raise StopIteration("This is it!")


it = fibonacci_sequence(10)
for x in it:
    print(x)
