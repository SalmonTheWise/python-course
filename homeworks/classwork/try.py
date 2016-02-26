__author__ = 'jack-a-lynn'
try:
    15/0
except ZeroDivisionError:
    print("IT'S ALIVE, ALIVE!")


def f(x):
    try:
        return 15/x
    except (TypeError, ZeroDivisionError) as err:
        print(type(err))
        print(err)
        print(err.args)


#print(f(4))
print(f(0))
#print(f([]))

# try:
#     x = open("test.txt", "r")
# except FileNotFoundError:
#     print("Too bad, file not found")
# else:
#     data = x.read()
#     print(data)

# def divide(x, y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print("/ZERO!!!")
#     else:
#         print("result is", result)
#     finally:
#         print("exec finally cause")
#
# divide(2, 1)
# divide(2, 0)
# divide(2, [])

def append(x, el):
    if not type(x) is list:
        raise TypeError("first arg should be list")
    else:
        x.append(el)

try:
    append("", 5)
except TypeError:
    print("type err")
    raise
