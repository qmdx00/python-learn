from scrapy import Spider, Item, Field

"""
github spider example
"""


class Repository(Item):
    url = Field()
    name = Field()


class Example(Spider):
    name = "github"
    start_urls = ["https://github.com/qmdx00?tab=repositories"]
    base = "https://github.com"

    def parse(self, response):
        """ 获取所有github仓库信息 """
        lis = response.css("div#user-repositories-list li")
        for li in lis:
            repo = Repository()
            repo['url'] = self.base + li.css('a::attr(href)')[0].extract()
            repo['name'] = li.css('a::text')[0].extract().strip().replace("\n", "")
            yield repo

# scrapy runspider example.py -o github.json -t json
