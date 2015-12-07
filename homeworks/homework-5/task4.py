__author__ = 'jack-a-lynn'
import re
import sys

comm = " *([#]+)"
as_t = " *([\w,. ]+) = "
str_ = 1

data = sys.stdin.read()
data = data.split('\n')

for l in data:
    if re.match(comm, l) is not None:
        str_ += 1
    else:
        res = re.match(as_t, l)
        if res is not None:
            answer = list(res.groups())
            for i in answer:
                print(str_, ' '.join(i.split(', ')))
        str_ += 1