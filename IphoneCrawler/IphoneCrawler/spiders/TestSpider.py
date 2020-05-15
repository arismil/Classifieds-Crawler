# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import open_in_browser


class PhoneSpider(scrapy.Spider):
    name = 'TestSpider'
    start_urls = ['https://www.insomnia.gr/classifieds/category/14-iphone/?filter=classifieds_type_1']

    def parse(self, response):
        iphone_links = response.css('.ipsTruncate ipsTruncate_line + a')
        print(iphone_links)
        yield from response.follow_all(iphone_links, self.parse_iphone)

        # pagination_links = response.css('li.ipsPagination_next a')
        # yield from response.follow_all(pagination_links, self.parse)

    def parse_iphone(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        open_in_browser(response)
        yield {
            'name': extract_with_css('h1.tittle-onestyle::text'),
            'date': response.xpath(
                '//*[@id="ipsLayout_mainArea"]/div/div[3]/div[1]/article/div[2]/div[2]/div[1]/p[4]/span[2]/span[@class="ipsDataItem_generic"]/text()').get(),
            'price': extract_with_css('.price grid__col-auto grid--justify-center::text'),
            'link': response
        }
