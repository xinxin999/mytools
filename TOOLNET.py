from lxml import etree
import requests
DOMAIN = "https://www.t00ls.net/articles-"
for i in range(1,60000):
    k = (DOMAIN + str(i))
    s = ".html"
    real = k + s
    url = real
    headers = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36"
    }
    resp = requests.get(url,headers=headers)
    text = resp.text
    html = etree.HTML(text)
    names = html.xpath("//h1[@class='entry_title entry-title']")
    for index in range(len(names)):
        print((names[index].text)+real)