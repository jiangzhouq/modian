# -*- coding=utf-8 -*-

import scrapy
import time
import logging
import requests

logger = logging.getLogger(__name__)
class modianSpider(scrapy.Spider):
    name = "huoguo"
    allowed_domains = ["modian.com"]
    #项目ID
    product_id = 80443
    #支持项ID，Like：reward-9
    item_id = [6]
    
    product_url = "https://zhongchou.modian.com/product_rewards/index?pid=" + str(product_id) + "&_mpos=pro_goback_web"
    start_urls = [
        product_url
    ] 
    
    def parse(self, response):
        wxurl = "https://sc.ftqq.com/SCU63006T23f45cef2f5637767bb29fbd42f9f8c65d907671c95c8.send"

        print '---------' + '\033[46m' + response.xpath('//h1/text()').extract()[0].encode("UTF-8") + '\033[0m'
        project_name = response.xpath('//h1/text()').extract()[0].encode("UTF-8")
        for sel_item_id in self.item_id:
            xpath_item_div = '//div[@for="reward-'+ str(sel_item_id) + '"][1]'
            item_div = response.xpath(xpath_item_div)
            item_name = item_div.xpath('.//span[@class="title"]/text()').extract()[0].encode("UTF-8") 
            if "已抢光" in item_div.xpath('.//p[@class="n"][1]/text()[1]').extract()[0].encode("UTF-8"):
                print '---------' + item_name
            else:
                print '---YES---' + item_name
                wxmessage = {"text":project_name, "desp":item_name}
                requests.get(wxurl, params=wxmessage)