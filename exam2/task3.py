__author__ = 'jack-a-lynn'
import requests
from lxml import etree

url = "http://larstheyeti.tumblr.com/"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter("content"):
    print(element.attrib[""])