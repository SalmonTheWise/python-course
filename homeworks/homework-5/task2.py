import re
import sys
data = sys.stdin.read()
number = data.split("\n")
list_ = []
for i in number:
    res = re.findall("0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}", i)
    if len(res) != 0:
        list_.append(i)
for i in list_:
    print(i)
