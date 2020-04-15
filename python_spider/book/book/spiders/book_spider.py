# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import BookItem


def parse_chapter(response: HtmlResponse):
    title = response.xpath("//div[@class='bookname']/h1//text()").getall()[0].split()
    text = response.xpath("//div[@id='content']//text()").getall()

    chapter_index = re.findall("\\d+", title[0])[0]
    chapter_title = title[1]
    chapter_content = "".join([x.strip() for x in text]).strip()

    yield BookItem(index=chapter_index, title=chapter_title, content=chapter_content)


class BookSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['230book.com']
    start_urls = ['https://www.230book.com/book/2526/']

    def parse(self, response):
        chapters = response.xpath("//ul[@class='_chapter']/li/a//@href").getall()

        for chapter in chapters:
            url = "https://www.230book.com/book/2526/" + chapter
            yield scrapy.Request(url, callback=parse_chapter)
