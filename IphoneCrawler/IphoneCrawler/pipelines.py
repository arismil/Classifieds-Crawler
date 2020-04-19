# -*- coding: utf-8 -*-
import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
# nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


# PROCESSING OF CLASSIFIED TO MODEL AND SIZE
class IphonecrawlerPipeline(object):
    def process_item(self, item, spider):
        if item["type"] is None:
            raise DropItem("δεν είναι πώληση")
        item.pop("type")
        return item
