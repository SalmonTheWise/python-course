import re
import sys
data = sys.stdin.read()
data = data.split("\n")
count = 1

for i in data:
    res = re.findall("(\w+) = ", i)
    if len(res) != 0:
        print(count, res[0])
    count += 1
