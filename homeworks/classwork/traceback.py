__author__ = 'jack-a-lynn'
import traceback

def a(i):
    b(i-1)


def b(i):
    if i > 0:
        a(i-1)
    else:
        traceback.print_()
