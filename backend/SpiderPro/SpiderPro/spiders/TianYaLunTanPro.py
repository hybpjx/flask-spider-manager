from copy import deepcopy

import scrapy


class TianyaluntanproSpider(scrapy.Spider):
    name = 'TianYaLunTanPro'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://bbs.tianya.cn/list.jsp?item=funinfo&nextid=1650943226000']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="main"]/div[7]/table//tr')
        item = {}
        for tr in tr_list:
            title:str = tr.xpath('./td[1]/a/text()').extract_first() or tr.xpath('./td[1]/a//text()')
            if title:
                item['title'] = title.replace("\r\n","").replace("\t","")
                title_url:str = tr.xpath("./td[1]/a/@href").extract_first()
                item['title_url'] = "http://bbs.tianya.cn"+title_url
                item['author'] = tr.xpath('./td[2]/a/text()').extract_first()
                item['click_number'] = tr.xpath('./td[3]/text()').extract_first()
                item['replies_number'] = tr.xpath('./td[4]/text()').extract_first()
                item['publish_date'] = tr.xpath('./td[5]/@title').extract_first()

                yield scrapy.Request(
                    url=item['title_url'],
                    callback=self.parse_detail,
                    meta={
                        "item":deepcopy(item)
                    }
                )
            else:
                pass

    def parse_detail(self,response):
        item = response.meta.get("item")
        item['description']=response.xpath('/html/head/meta[@name="description"]/@content').extract_first()
        yield item