# -*- coding: utf-8 -*-

import scrapy


class IphonespiderSpider(scrapy.Spider):
    name = 'IphoneSpider'
    start_urls = ['https://www.insomnia.gr/classifieds/category/14-iphone/']

    def parse(self, response):
        SET_SELECTOR = 'li.ipsDataItem'
        for iphone in response.css(SET_SELECTOR):
            PRICE_SELECTOR = './div[1]/p/span/strong/text()'
            NAME_SELECTOR = './div[2]/h4/div/a/text()'
            CLASSIFIED_TYPE_SELECTOR = './div[3]/ul/li[1]/span[@class="ipsBadge ipsBadge_positive"]/text()'
            yield {
                'name': iphone.xpath(NAME_SELECTOR).get(),
                'price': iphone.xpath(PRICE_SELECTOR).get(),
                'type': iphone.xpath(CLASSIFIED_TYPE_SELECTOR).get()
            }
            NEXT_PAGE_SELECTOR = '/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/ul/li[@class="ipsPagination_next"]/a/@href'
            next_page = response.xpath(NEXT_PAGE_SELECTOR).get()
            if next_page:
                print(next_page)
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
