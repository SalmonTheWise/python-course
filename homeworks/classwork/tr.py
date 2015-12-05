__author__ = 'jack-a-lynn'
from lxml import etree

tree = etree.parse("test.xml").getroot()

sum = 0
for score in tree.iter("score"):
    sum += int(score.text)
mean = sum / len(list(tree.iter("score")))
print(mean)
