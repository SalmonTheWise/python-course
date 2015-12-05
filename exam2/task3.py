__author__ = 'jack-a-lynn'
import requests
from lxml import etree

url = "https://twitter.com/googlefacts"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for element in tree.iter("tweet"):
    print(element.attrib["TweetTextSize TweetTextSize--16px js-tweet-text tweet-text"])