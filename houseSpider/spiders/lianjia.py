# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from houseSpider.items import LianjiaItem


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['wh.lianjia.com']
    start_urls = ['http://wh.lianjia.com/ershoufang']

    # 每一页的匹配规则
    pageLink = LinkExtractor(allow=r'/ershoufang/pg\d+')

    # 每个房源详情页的匹配规则
    contentlink = LinkExtractor(allow=r'/ershoufang/\d+.html')


    rules = [
        Rule(pageLink),
        Rule(contentlink, callback="parseContent", follow=False),
    ]

    # def parseContent(self, response):
    def parseContent(self, response):

        item = LianjiaItem()
        # print("1123123131231313123131")

        title = response.xpath("//div[@class='title']/h1/text()").extract()
        communityName = response.xpath("//div[@class='communityName']/a/text()").extract()
        areaName = response.xpath("//div[@class='areaName']//a/text()").extract()
        totalPrice = response.xpath("//div[@class='price ']/span/text()").extract()
        unitPrice = response.xpath("//div[@class='unitPrice']/span/text()").extract()

        print(title)
        print(communityName)
        print(areaName)
        print(totalPrice)
        print(unitPrice)

        item['detailLink'] = response.url
        item['title'] = title[0].strip()
        item['communityName'] = communityName[0].strip()
        item['areaName'] = " ".join(areaName)
        item['totalPrice'] = totalPrice[0].strip()
        item['unitPrice'] = unitPrice[0].strip()

        print("----------")
        print(item['areaName'])

        yield item







        # print("1111111")
        # filename = "house.html"
        # open(filename, 'wb+').write(response.body)
        # print("2222222")

        items = []
        #
        # city = response.xpath("//div[@class='resultDes clear']//h2/text()").extract()
        # city = city[1][1:-3]
        # print(city)

        # for each in response.xpath("//ul/li[@class='clear LOGCLICKDATA']"):
        #     item = LianjiaItem()
        #
        #     title = each.xpath("div/div[@class='title']/a/text()").extract()
        #
        #     detaisLink = each.xpath("div/div[@class='title']/a/@href").extract()
        #
        #     address = each.xpath("div/div[@class='address']//a/text()").extract()
        #
        #     houseIcon = each.xpath("div//div[@class='houseInfo']/text()").extract()
        #
        #     positionIcon = each.xpath("div/div[@class='flood']//div/text()").extract()
        #
        #     businessArea = each.xpath("div/div[@class='flood']//a/text()").extract()
        #
        #     # unit = each.xpath("div/div[@class='priceInfo']//div/text()").extract()
        #
        #     totalPrice = each.xpath("div//div[@class='totalPrice']/span/text()").extract()
        #
        #     unitPrice = each.xpath("div//div[@class='unitPrice']/span/text()").extract()
        #
        #     print(title)
        #     print(detaisLink)
        #     print(address)
        #     print(houseIcon)
        #     print(positionIcon)
        #     print(businessArea)
        #     # print(unit)
        #     print(totalPrice)
        #     print(unitPrice)
        #
        #     item['title'] = title[0].strip()
        #     item['address'] = address[0].strip()
        #     item['houseIcon'] = houseIcon[0].strip()
        #     item['positionIcon'] = positionIcon[0].strip()
        #     item['businessArea'] = businessArea[0].strip()
        #     item['totalPrice'] = totalPrice[0].strip()
        #     item['unitPrice'] = unitPrice[0].strip()
        #
        #     item['detaisLink'] = detaisLink[0].strip()
        #     # item['city'] = city
        #
        #     # items.append(item)
        #
        #     print("-------------")
        #
        #     yield item

        # return items



