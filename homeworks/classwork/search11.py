import requests
from lxml import etree

url = "http://larstheyeti.tumblr.com/"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter("img"):
    print(element.attrib["src"])
