import scrapy

class SampleSpider(scrapy.Spider):
    name = 'sample'
    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com/']

    def parse(self, response):
        print(response.text)
