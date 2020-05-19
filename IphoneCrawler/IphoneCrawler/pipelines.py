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

        if re.match(r"\d+", item["price"]) is None:  # αν δεν έχει τιμή τότε πέταμα
            raise DropItem("δεν έχει τιμή")
        if re.match(r"\d+", item["date"]) is None:  # αν δεν έχει ημερομηνία τότε πέταμα
            raise DropItem("δεν έχει ημερομηνία")
        return item
