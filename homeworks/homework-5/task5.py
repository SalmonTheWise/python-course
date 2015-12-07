__author__ = 'jack-a-lynn'
import re
import sys

data = sys.stdin.read()

txt = re.sub('(\W)+', " ", data)
print(txt)
