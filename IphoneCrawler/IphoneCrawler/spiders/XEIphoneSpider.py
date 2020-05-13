# -*- coding: utf-8 -*-
import scrapy


class XeiphonespiderSpider(scrapy.Spider):
    name = 'XEIphoneSpider'
    start_urls = ['https://www.xe.gr/search?Item.category__hierarchy=117147&Item.make=115135&Item.master_type=114579&System.item_type=xe_stelexos&Transaction.type_channel=117518&per_page=50&sort_by=Publication.effective_date_start&sort_direction=desc&Geo.area_id_new__hierarchy=82196']

    def parse(self, response):
        SET_SELECTOR = '#xeResultsColumn'
        for iphone in response.css(SET_SELECTOR):
            pass


