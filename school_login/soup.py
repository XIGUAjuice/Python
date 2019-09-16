# %%
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import requests


def get_urls(filename):
    with open(filename, encoding='utf-8') as html:
        base_url = "http://xsgl.7i5q.cas.scut.edu.cn/"
        urls = []
        bs = BeautifulSoup(html)
        href_list = bs.find_all(name='a', attrs={'href': re.compile("^/")})
        for item in href_list:
            url = urljoin(base_url, item.get("href"))
            urls.append(url)
        return urls


s = requests.Session()
headers = {
    'Cookie': 'JSESSIONID=05F359F59BE379B39186282A1087BAF8.student48_2; Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616=1567861926,1567864866,1567929025,1567948299; JSESSIONID=BDB27D917C89AE2453019CC860445693.student51_3; Hm_lpvt_cad45348d1fdf49a7a9a1f8b99526616=1567990991',
}
scores = {}


def get_self_ex(bs):
    score_self = 0
    score_ex = 0
    # 自评分
    score_self = float(
        bs.find(name="td", string=re.compile("合计")).find_next('td').string)

    # 加分项
    rows_passed = bs.find('td', string=re.compile("测评加分")).find_all_next(
        name='td', string=re.compile("班级通过"))
    for item in rows_passed:
        score_ex = score_ex + float(item.find_previous('td').string)
    score = score_self + score_ex
    return score


def get_morral_scores():
    urls = get_urls("德育名单.html")
    for url in urls[1:]:
        try:
            response = s.get(url, headers=headers)
            bs = BeautifulSoup(response.content.decode())
            score_self_ex = 0
            score = 0

            # 姓名
            name_str = bs.find(name='td', string=re.compile("学生")).string
            name = re.match(r"学生：(\S*)", name_str.strip()).group(1)
            scores.setdefault(name, {})

            # 自评分和加分
            score_self_ex = get_self_ex(bs)

            score = score_self_ex
            scores[name]["德育分"] = score
        except AttributeError:
            print(f"-------------{url}-----------failed!!")
            continue


def get_sports_scores():
    urls = get_urls("文体名单.html")
    for url in urls[1:]:
        try:
            response = s.get(url, headers=headers)
            bs = BeautifulSoup(response.content.decode())
            score_class = 0
            score_self_ex = 0
            score = 0

            name_str = bs.find(name='td', string=re.compile("学生")).string
            name = re.match(r"学生：(\S*)", name_str.strip()).group(1)

            # 体育课分
            rows_class = bs.find("table", attrs={'class': 'List'}).find_all(
                "td", string=re.compile("班级通过"))
            for item in rows_class:
                score_class = score_class + \
                    float(list(item.previous_siblings)[7].string.strip())

            # 自评分和加分项
            score_self_ex = get_self_ex(bs)

            score = score_class / 2 * 0.55 + score_self_ex
            scores[name]["文体分"] = score
        except AttributeError:
            print(f"-------------{url}-----------failed!!")
            continue


def get_smart_scores():
    urls = get_urls("智育名单.html")
    for url in urls[1:]:
        try:
            response = s.get(url, headers=headers)
            bs = BeautifulSoup(response.content.decode())
            score_self_ex = 0
            score_class = 0
            credit_class = 0
            total_score = 0
            score = 0

            # 姓名
            name_str = bs.find(name='td', string=re.compile("学生")).string
            name = re.match(r"学生：(\S*)", name_str.strip()).group(1)

            # 课程分
            rows_class = bs.find_all(
                "td", string=re.compile("必修课和专业必修课（或限定选修课）"))
            for item in rows_class:
                row = list(item.previous_siblings)

                # 成绩
                score_class = row[3].string.strip()
                score_class = float(re.findall(r"\d+\.?\d*", score_class)[0])

                # 学分
                credit_class = row[1].string.strip()
                credit_class = float(re.findall(r"\d+\.?\d*", credit_class)[0])

                total_score = total_score + score_class * credit_class

            # 自评分和加分项
            score_self_ex = get_self_ex(bs)

            score = total_score * 2 / 100 + score_self_ex
            scores[name]["智育分"] = score
        except (AttributeError, KeyError):
            print(f"-------------{url}-----------failed!!")
            continue


get_morral_scores()
get_sports_scores()
get_smart_scores()

result = {}
for name, data in scores:
    result[name] = round(data["智育分"] * 0.65 + data["德育分"]
                         * 0.2 + data["文体分"] * 0.15, 2)

sorted(result.items(), key=lambda x: x[1], reverse=True, )
print(result)
# %%
