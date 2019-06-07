from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = []


def get_links(url):
    global pages
    url = (quote("https://baike.baidu.com" + url, safe=":%/"))
    html = urlopen(url)
    soup = BeautifulSoup(html)

    print(soup.h1.string)
    print(soup.find("div", {"class": "para", "label-module": "para"}).get_text())

    links = soup.find("div", {"class": "content-wrapper"}).find_all("a", href=re.compile(r"^(/item/).*$"))
    try:
        newpage = links[random.randint(0, len(links) - 1)].attrs['href']
    except ValueError:
        newpage = pages[random.randint(0, len(pages) - 1)]
    if newpage not in pages:
        print("------------------------------------------" + newpage)
        pages.append(newpage)
    get_links(newpage)
    # for a in soup.find("div", {"class": "content-wrapper"}).find_all("a", href=re.compile(r"^(/item/).*$")):
    #     if 'href' in a.attrs:
    #         if a.attrs['href'] not in pages:
    #             newpage = a.attrs['href']
    #             print("-------------------------------" + newpage)
    #             pages.add(newpage)
    #             get_links(newpage)


random.seed(datetime.datetime.now())
get_links("/item/百度")
