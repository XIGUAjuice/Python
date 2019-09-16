# %%
import requests
from bs4 import BeautifulSoup
import random
import re

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080'
}

def get_links(article_url):
    response = requests.get("https://en.wikipedia.org/wiki/{}".format(article_url), proxies=proxies)
    bsobj = BeautifulSoup(response.text)
    return bsobj.find("div", {'id': 'bodyContent'}).find_all("a", {'href': re.compile("^(/wiki/)((?!:).)*$")})

# %%
