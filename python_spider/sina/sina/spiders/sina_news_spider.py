# coding=utf-8
import re
import scrapy
from bs4 import BeautifulSoup
from ..items import SinaItem

"""
新浪新闻爬虫
"""


class SinaNewsSpider(scrapy.Spider):
    name = "sina_news"
    start_urls = ["https://news.sina.com.cn/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for tag in soup.find_all('a', href=re.compile(r"^http.*\d{4}-\d{2}-\d{2}.*shtml$")):
            item = SinaItem()
            item['url'] = tag.get('href')
            item['title'] = tag.text.strip()
            print(item)
            yield item
