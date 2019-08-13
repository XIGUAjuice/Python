from urllib.request import urlopen
from urllib.parse import quote, urljoin
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = []


def get_links(url):
    """ 寻找百度百科中的百科链接，不断跳转 """
    global pages
    url = quote(url, safe=":%/?=#")
    html = urlopen(url)
    soup = BeautifulSoup(html)

    # 打印第一段
    try:
        print(soup.h1.string)
        print(soup.find("div", {"class": "para", "label-module": "para"}).get_text())
    except AttributeError:
        print("找不到对应内容")

    # 寻找百科连接
    links = soup.find_all("a", href=re.compile(r"^(/item/).*$"))
    newpage = links[random.randint(0, len(links) - 1)].attrs['href']
    # newpage = pages[random.randint(0, len(pages) - 1)]

    # 解析成完整url
    newpage = urljoin(url, newpage)

    # 找到新页面
    if newpage not in pages:
        print("------------------------------------------" + newpage)
        pages.append(newpage)

    get_links(newpage)


random.seed(datetime.datetime.now())
get_links("https://baike.baidu.com/item/创意设计")
