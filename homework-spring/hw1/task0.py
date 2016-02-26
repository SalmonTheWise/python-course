__author__ = 'jack-a-lynn'

def sum(a, b):
    if type(a) == int and type(b) == int:
        if a >= 0 and b >= 0:
            return int(a) + int(b)
        else:
            raise ValueError
    else:
        raise TypeError


