from urllib.request import urlopen
from urllib.parse import quote, urlparse, urljoin
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
import re
import random

pages = []


def get_internal_links(url):
    """ 获取页面中的内链 """
    internal_links = []

    url = quote(url, safe=":%/?=#&")
    try:
        html = urlopen(url)
    except HTTPError:
        get_internal_links(pages[random.randint(len(pages) - 1)])
    soup = BeautifulSoup(html, "html.parser")
    include_url = urlparse(url).netloc

    # print(url)
    # print(soup)
    for a in soup.findAll("a", href=re.compile(r"^(((?!(http|mail|javascript|tel)).)*)|(.*("+include_url+"))$")):
        link = a.attrs['href']
        # 如果link不在内链列表中，则拼接成完整url存入
        if link not in internal_links:
            internal_link = urljoin(url, link)
            internal_links.append(internal_link)
    return internal_links


def get_external_links(url):
    """ 获取页面中所有的外链 """
    external_links = []

    url = quote(url, safe=":%/?=#&")
    try:
        html = urlopen(url)
    except HTTPError:
        get_external_links(pages[random.randint(0, len(pages) - 1)])
    soup = BeautifulSoup(html, "html.parser")
    exclude_url = urlparse(url).netloc

    for a in soup.find_all("a", href=re.compile("^(http|www)((?!"+exclude_url+").)*$")):
        link = a.attrs['href']
        if link not in external_links:
            external_links.append(link)
    return external_links


def random_link(url):
    """ 递归地访问外链 """
    global pages
    url = quote(url, safe=":%/?=#&")

    external_links = get_external_links(url)
    if len(external_links) == 0:
        # 该页面无外链，则寻找内链，再在其中找外链
        internal_links = get_internal_links(url)
        if len(internal_links) == 0:
            # 也没有内链
            url = pages[random.randint(0, len(pages) - 1)]
        else:
            url = internal_links[random.randint(0, len(internal_links) - 1)]
    else:
        url = external_links[random.randint(0, len(external_links) - 1)]

    if url not in pages:
        print(url)

        try:
            html = urlopen(url)
        except HTTPError:
            random_link(pages[random.randint(0, len(pages) - 1)])

        soup = BeautifulSoup(html, "html.parser")

        try:
            print(soup.title.string)
        except AttributeError:
            print("no title")
        print("-------------------------------------------")
        pages.append(url)

    random_link(url)


random.seed(datetime.now())
random_link("http://www.xuetangx.com")
# print(get_external_links("https://baike.baidu.com/item/正则表达式"))