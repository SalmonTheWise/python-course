__author__ = 'jack-a-lynn'
import requests
from lxml import etree

url = requests.get('https://twitter.com/googlefacts').text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter("p"):
    if "class" in tweet.attrib:
