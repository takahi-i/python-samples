import lxml.html
import requests

url = 'http://unigram.org/index.html'
r = requests.get(url) 
html = lxml.html.fromstring(r.text)

for title in html.cssselect(".product > .title > a"):
    if title.text:
        print(title.text)
