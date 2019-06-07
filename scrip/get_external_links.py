from urllib.request import urlopen
from urllib.parse import quote, urlparse, urljoin
from bs4 import BeautifulSoup
from datetime import datetime
import re
import random


def get_internal_links(soup, url):
    """ 获取页面中的内链 """
    internal_links = []
    include_url = urlparse(url).netloc
    for a in soup.findAll("a", href=re.compile(r"^(?!http)(?!mail)(?!javascript)|.*("+include_url+")")):
        link = a.attrs['href']
        # 如果link不在内链列表中，则拼接成完整url存入
        if link not in internal_links:
            internal_link = urljoin(url, link)
            internal_links.append(internal_link)
    return internal_links


# 找出所有外链
random.seed(datetime.now())
url = "https://www.hao123.com/?tn=95752409_hao_pg"
html = urlopen(url)
soup = BeautifulSoup(html)
external_links = []
exclude_url = urlparse(url).netloc
for a in soup.find_all("a", href=re.compile("^(http|www)((?!"+exclude_url+").)*$")):
    link = a.attrs['href']
    if link not in external_links:
        print(link)
        external_links.append(external_links)
print(len(external_links))
