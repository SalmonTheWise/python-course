import requests
import re

links = []
with open('links.txt', 'r') as f:
    for line in f:
        links.append(line.strip())

emails = set()
for link in links:
    d = requests.get(lnk)
    mails = re.findall('[.\w]+@[.\w]+', d.text)
    for mail in mails:
