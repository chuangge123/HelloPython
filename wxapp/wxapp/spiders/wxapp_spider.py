# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem



class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        # callback = 'parse_item',这里不需要回调函数，也就是不需要进行解析操作，因为我们要进入这个页面所有存放具体内容的页面去爬取东西。
        Rule(LinkExtractor(allow=r".+article-.+\.html"), callback="parse_detall", follow=False)

    )

    def parse_detall(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author_1=response.xpath("//p[@class='authors']")
        author=author_1.xpath(".//a/text()").get()
        put_time=author_1.xpath("//span[@class='time']/text()").get()
        article_content=response.xpath("//td[@id='article_content']//text()").getall()
        content="".join(article_content).strip()
        item = WxappItem(title=title,author=author,put_time=put_time,content=content)
        yield item
