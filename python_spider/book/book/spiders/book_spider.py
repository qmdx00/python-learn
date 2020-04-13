# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import BookItem


def parse_chapter(response: HtmlResponse):
    title = response.xpath("//div[@class='bookname']/h1//text()").getall()
    title_index = re.findall("\\d+", "".join(title).strip())[0]
    text = response.xpath("//div[@id='content']//text()").getall()
    content = "".join([x.strip() for x in text]).strip()

    yield BookItem(title=title_index, content=content)


class BookSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['230book.com']
    start_urls = ['https://www.230book.com/book/2526/']

    def parse(self, response):
        chapters = response.xpath("//ul[@class='_chapter']/li/a//@href").getall()

        for chapter in chapters:
            url = "https://www.230book.com/book/2526/" + chapter
            yield scrapy.Request(url, callback=parse_chapter)
