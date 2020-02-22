from lxml import etree
import requests
DOMAIN = "https://xz.aliyun.com/t/"
for i in range(721,7243):
    k = (DOMAIN + str(i))
    url = k
    headers = {
        "User-Agent":"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
    }
    resp = requests.get(url,headers=headers)
    text = resp.text
    html = etree.HTML(text)
    names = html.xpath("//span[@class='content-title ']")
    for index in range(len(names)):
        print((names[index].text)+k)