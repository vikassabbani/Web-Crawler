import scrapy
from ..items import WebspyderItem


class Quotespyder(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        items = WebspyderItem()
        quotess = response.css('div.quote')

        for quotes in quotess:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('small.author::text').extract()
            tag = quotes.css('a.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = 'http://quotes.toscrape.com/page/' + str(Quotespyder.page_number) + '/'
        print(next_page)
        if Quotespyder.page_number < 11:
            Quotespyder.page_number += 1
            yield response.follow(next_page, callback= self.parse)