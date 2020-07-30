# -*- coding: utf-8 -*
import re
f = open("dg.txt", "r", encoding='utf-8')     
data = f.readlines()                            
f.close()                                       
for line in data:
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    string = str(line)
    url = re.findall(pattern,string)
    f1 = open("url.txt", "a+", encoding='utf-8')
    for urls in url:
        f1.write(urls+'\n')
    f1.close()