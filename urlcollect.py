import re
import requests
import random
from lxml import etree
from fake_useragent import UserAgent
ua = UserAgent()
sousuolist = ["inurl:jsp?id=","inurl:aspx?id=","inurl:asp?id=","inurl:admin/login"]      #百度语法搜索，表哥们可以宁外加一些语句，之所以没有加php，是因为百度搜的php完全没有php

def getip():                                  #爬取代理IP，表哥们也可以爬取其他的
    url = "http://proxylist.fatezero.org/proxy.list"
    headers = {
        "User-Agent": ua.random,
            }
    resp = requests.get(url, headers=headers)
    text = resp.text
    ssl = re.findall(r'"type": "(.*?)"', text)
    ip = re.findall(r'"host": "(.*?)"', text)
    port = re.findall(r'"port": (.*?),', text)
    realurl = ('\n'.join([str(i[0]) + str("://") + str(i[1]) + str(":") + str(i[2]) for i in zip(ssl, ip, port)]))
    #print(realurl)
    f1 = open("daili.txt", "a+", encoding='utf-8')
    f1.write(realurl)
    f1.close()
#getip()

def httpip():                          #此函数是过滤http的代理是否可用
    f = open("daili.txt", "r", encoding='utf-8')
    data = f.readlines()
    f.close()
    for line in data:
        flter = "http://"
        ok = flter in line
        if bool(ok) == True:
            try:
                resp = requests.get('http://www.baidu.com/', proxies={"http": line}, timeout=2)
            except:
                print('connect failed')
            else:
                if (resp.status_code) == 200:
                    http = (line.strip("http://"))
                    f1 = open("http.txt", "a+", encoding='utf-8')
                    f1.write(http)
                    f1.close()
#httpip()

def httpsip():         #和上面函数一样
    f = open("daili.txt", "r", encoding='utf-8')
    data = f.readlines()
    f.close()
    for line in data:
        flter = "https"
        ok = flter in line
        if bool(ok) == True:
            https = (line.strip("https://"))
            url = "http://www.baidu.com/"
            headers = {"User-Agent": ua.random, }
            proxies = {"https": https, }
            try:
                res = requests.get(url, proxies=proxies, headers=headers, timeout=2)
                if (res.status_code) == 200:
                    f1 = open("https.txt", "a+", encoding='utf-8')
                    f1.write(https)
                    f1.close()
            except Exception as e:
                pass
#httpsip()

def function1urlcoolect():                 #信息搜集，爬取百度的url
    for urls in sousuolist:
        aa = str(urls)
        for b in range(0, 201, 10):              #这个是页数，我默认调的20页
            x = str(b)
            url = "https://www.baidu.com/s?wd=" + aa + "&pn=" + x + "&ie=utf-8&rsv_pq=d9aea5c300020ea1&rsv_t=80abfpCuSVYp2OuZGqg%2FDifuo7RBscY63qXR8Hi4r2bE1bHBDcQUues7H2o"
            with open('http.txt') as f:
                lines = f.readlines()
                f.close()
                for i in range(1, 30):            #可能我过滤的方法有问题，有的测试成功的代理ip还是要链接超时
                    try:
                        meanless = "http://" + random.choice(lines)
                        proxiesiphttp = meanless
                        headers = {
                            "Host": "www.baidu.com",
                            "User-Agent": ua.random,
                        }
                        proxies = {"http": proxiesiphttp, }
                        resp = requests.get(url, headers=headers, proxies=proxies, timeout=3)
                        text = resp.content.decode('utf-8')
                        urllinks = re.findall(r'target="_blank" href="(.*?)" class="c-showurl', text)
                        for yuanshu in urllinks:
                            r = requests.get(yuanshu)
                            f1 = open("urlcollect.txt", "a+", encoding='utf-8')
                            f1.write((r.url) + '\n')
                            f1.close()
                            print(r.url)
                        break
                    except:                                                 #如果代理pi链接超时，将其从表单移除
                        with open('http.txt', 'r') as r:
                            meiyongde = str(proxiesiphttp)
                            r.close()
                        with open('http.txt', 'w') as w:
                            for l in lines:
                                if meiyongde not in l:
                                    w.write(l)
#function1urlcoolect()

def xinxifenlei():                                               #将信息分类
    with open('urlcollect.txt') as f:
        line = f.readlines()
        lines = {}.fromkeys(line).keys()
        f.close()
        for data in lines:
            if bool(re.findall('(aspx)(\?)',data)) ==True:
                f1 = open("aspxurl.txt", "a+", encoding='utf-8')
                f1.write(data)
                f1.close()
            if bool(re.findall('(jsp)(\?)',data)) ==True:
                f1 = open("jspurl.txt", "a+", encoding='utf-8')
                f1.write(data)
                f1.close()
            if bool(re.findall('(asp)(\?)',data)) ==True:
                f1 = open("aspurl.txt", "a+", encoding='utf-8')
                f1.write(data)
                f1.close()
            if bool(re.findall('(admin.)|(login.)|(adminlogin)',data)) ==True:
                f1 = open("houtai.txt", "a+", encoding='utf-8')
                f1.write(data)
                f1.close()
#xinxifenlei()

