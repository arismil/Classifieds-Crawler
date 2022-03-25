# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser


class PhoneSpider(scrapy.Spider):
    name = 'TestSpider'
    start_urls = ['https://www.insomnia.gr/classifieds/category/15-ipad/?filter=classifieds_type_1']

    def parse(self, response):
        iphone_links = response.css('.ipsType_break > a')

        yield from response.follow_all(iphone_links, self.parse_iphone)

        pagination_links = response.css('li.ipsPagination_next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_iphone(self, response):
        NAME_SELECTOR = 'div.ipsType_break.ipsContained > span'
        NAME_CSS = response.css(NAME_SELECTOR)
        VIEWS_SELECTOR = 'span.value.views-spanblock'
        VIEWS_CSS = response.css(VIEWS_SELECTOR)
        DATE_SELECTOR = 'p.serial > span.value > span'
        DATE_CSS = response.css(DATE_SELECTOR)
        PRICE_SELECTOR = 'div.worthit > div > div > p'
        PRICE_CSS = response.css(PRICE_SELECTOR)
        yield {
            'name': NAME_CSS.xpath('./text()').get(),
            'date': DATE_CSS.xpath('./text()').get(),
            'price': PRICE_CSS.xpath('./text()').get(),
            'views': VIEWS_CSS.xpath('./text()').get(),
            'link': response.url
        }
