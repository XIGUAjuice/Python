# %%
import execjs
import requests
import re
from bs4 import BeautifulSoup


# def get_cookie(response):
#     # 获取cookie
#     set_cookie = response.headers["set-Cookie"]
#     jsessionid = re.search("(JSESSIONID=[0-9A-Z]*)", set_cookie)[0]
#     language = "Language=zh_CN"
#     clwz = re.search(r"(clwz_blc_pst_SSO=(\.|[0-9])*)", set_cookie)[0]
#     cookie = jsessionid + "; " + language + "; " + clwz
#     return cookie


def get_lt(response):
    bs = BeautifulSoup(response.content.decode())
    lt = bs.find("input", attrs={"id": "lt"})["value"]
    return lt


def get_rsa(username, password, lt):
    """ 进行加密 """
    origin_str = username + password + lt
    rsa = str_enc.call("strEnc", origin_str, "1", "2", "3")
    return rsa


def login(login_url, username, password, response, session):
    """ 登录 返回session """
    lt = get_lt(response)
    ul = str(len(username))
    pl = str(len(password))
    rsa = get_rsa(username, password, lt)
    # cookie = get_cookie(response)

    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '349',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'JSESSIONID=88484B4B31F3D7CB7C85CFEA2B80AC80; Language=zh_CN; clwz_blc_pst_SSO=96544458.38943',
        # 'Host': 'sso.scut.edu.cn',
        # 'Origin': 'xsjw2018.scuteo.com',
        # 'Referer': 'https://sso.scut.edu.cn/cas/login?service=http%3A%2F%2Fxsjw2018.scuteo.com%2Fsso%2Fdriotlogin',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-User': '?1',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }

    data = {
        "rsa": rsa,
        "ul": ul,
        "pl": pl,
        "lt": lt,
        "execution": "e1s1",
        "_eventId": "submit",
    }

    login_response = session.post(login_url, data=data, headers=headers, allow_redirects=True)
    return login_response

with open("des.js", "r") as f:
    js = f.read()

str_enc = execjs.compile(js)
login_url = "https://sso.scut.edu.cn/cas/login?service=http%3A%2F%2Fxsjw2018.scuteo.com%2Fsso%2Fdriotlogin"
session = requests.Session()
response = session.get(login_url)
login_response = login(login_url, "201830612290", "SCut2218", response, session)



# %%
