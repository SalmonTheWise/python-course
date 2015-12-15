import re
import requests

url_beg = 'https://en.wikipedia.org/wiki/Gone_Maggie_Gone'
url_end = 'https://en.wikipedia.org/wiki/Theia_(planet)'


def get_links(url):
    data = requests.get(url).text
    raw_urls = re.findall(r'href=[\'"]?/wiki/([^\'" >]+)', data)
    cnt = 0
    while cnt < len(raw_urls):
        if ':' in raw_urls[cnt]:
            del raw_urls[cnt]
        elif 'Main_Page' in raw_urls[cnt]:
            del raw_urls[cnt]
        else:
            cnt += 1
    urls = set(raw_urls)
    links = ["https://en.wikipedia.org/wiki/" + url for url in urls]
    return links


def game(url_1, url_2):
    links = get_links(url_1)
    if url_2 in links:
        print(url_1)
        print(url_2)
    else:
        for link in links:
            link2s = get_links(link)
            if url_2 in link2s:
                print(url_1)
                print(link)
                print(url_2)
                break
            else:
                for link2 in link2s:
                    link3s = get_links(link2)
                    if url_2 in link3s:
                        print(url_1)
                        print(link2)
                        print(url_2)
                        break
                    else:
                        for link3 in link3s:
                            link4s = get_links(link3)
                            if url_2 in link4s:
                                print(url_1)
                                print(link3)
                                print(url_2)
                                break

print(game(url_beg, url_end))
