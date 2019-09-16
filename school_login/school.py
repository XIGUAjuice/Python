import requests

s = requests.Session()

headers = {
    'Cookie': 'JSESSIONID=05F359F59BE379B39186282A1087BAF8.student48_2; Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616=1567861926,1567864866,1567929025,1567948299; JSESSIONID=BDB27D917C89AE2453019CC860445693.student51_3; Hm_lpvt_cad45348d1fdf49a7a9a1f8b99526616=1567990991',
}

url = "http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp"
response = s.get(url, headers=headers)

with open("智育名单.html", "w", encoding='utf-8') as f:
    f.write((response.content.decode()))
