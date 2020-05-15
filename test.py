# -*- coding: utf-8 -*-

import scrapy


class IphonespiderSpider(scrapy.Spider):
    name = 'IphoneSpider'
    start_urls = ['https://www.insomnia.gr/classifieds/category/14-iphone/?filter=classifieds_type_1']

    def parse(self, response):
        SET_SELECTOR = 'li.ipsDataItem'
        for iphone in response.css(SET_SELECTOR):
            PRICE_SELECTOR = './div[1]/p/span/strong/text()'
            NAME_SELECTOR = './div[2]/h4/div/a/text()'
            CLASSIFIED_TYPE_SELECTOR = './div[3]/ul/li[1]/span[@class="ipsBadge ipsBadge_positive"]/text()'
            LINK_SELECTOR = './div[2]/h4/div/a/@href'
            PRODUCT_PAGE_LINK = iphone.xpath(LINK_SELECTOR).get()
            iphone_item = {
                'name': iphone.xpath(NAME_SELECTOR).get(),
                'price': iphone.xpath(PRICE_SELECTOR).get(),
                'type': iphone.xpath(CLASSIFIED_TYPE_SELECTOR).get(),
                'link': iphone.xpath(LINK_SELECTOR).get(),
            }
            yield scrapy.Request(PRODUCT_PAGE_LINK, callback=self.parse_iphone_date, cb_kwargs=iphone_item)
            # NEXT_PAGE_SELECTOR = '/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/ul/li[@class="ipsPagination_next"]/a/@href'
            # next_page = response.xpath(NEXT_PAGE_SELECTOR).get()
            # if next_page is not None:
            #
            #     yield scrapy.Request(next_page,callback=self.parse)

    def parse_iphone_date(self, response, name, price, type, link):
        date = response.xpath(
            '//*[@id="ipsLayout_mainArea"]/div/div[3]/div[1]/article/div[2]/div[2]/div[1]/p[4]/span[2]/span[@class="ipsDataItem_generic"]/text()').get()

        yield dict(name=name, price=price, type=type, link=link, date=date)
