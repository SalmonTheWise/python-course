__author__ = 'jack-a-lynn'

n = int(input())
stack = input().split(" ")
m = int(input())

rules = {}

for i in range(m):
    fun, ex1, ex2 = input().split(" ")
    if fun not in rules:
        rules[fun] = {ex1: ex2}
    else:
        rules[fun][ex1] = ex2

active_exception = input()
i = len(stack) - 1

while i > 0:
    fun = stack[i]
    if active_exception in rules[fun]:
        if rules[fun][active_exception] == " ":
            break
        active_exception = rules[fun][active_exception]
        i -= 1

print(" ".join(stack[i + 1]))