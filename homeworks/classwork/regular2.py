__author__ = 'jack-a-lynn'
import re
import requests
from urllib.parse import urlencode

while True:
    gene = input()
    query = {"text": gene}
    query_string = urlencode(query)
    url_gene = "https://www.yandex.ru/search/?" + query_string
    response = requests.get(url_gene)

    text = response.text

    results = re.findall("(https://en.wikipedia.org/wiki/(\w+))", text)
    print(results)

