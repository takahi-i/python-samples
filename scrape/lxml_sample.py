import lxml.html
import requests

url = 'http://unigram.org/index.html'
r = requests.get(url) 
html = lxml.html.fromstring(r.text)
title = html.xpath('//*[@id="content"]/div[2]/div[1]/h4/a[1]/text()') # xpath copied from unigram.org
print(title)
