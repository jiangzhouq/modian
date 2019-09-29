# -*- coding=utf-8 -*-

import scrapy
import telegram 
import time
import logging

logger = logging.getLogger(__name__)
class modianSpider(scrapy.Spider):
    name = "biu"
    allowed_domains = ["modian.com"]
    #项目ID
    product_id = 65696
    #支持项ID，Like：reward-9
    item_id = [2]
    
    product_url = "https://zhongchou.modian.com/product_rewards/index?pid=" + str(product_id) + "&_mpos=pro_goback_web"
    start_urls = [
        product_url
    ] 
    
    def parse(self, response):
        bot = telegram.Bot(token='823530794:AAGk2v80sSgevtLMivvLcwJnRvrGiWsb0ns')
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
                bot.sendMessage(chat_id=791147649, text=project_name + "\n" + item_name)
            
            
#        print('\033[1;31;40m')
#        if len(list) == 0:
#               print '无此项，请检查。'
#        else:
#            if "已抢光" in list[0].encode("UTF-8"):
#                print list[0]
#            else:
#                print 'result : bitch you are here!!!!!!!!!!!!!!!'
#                bot.sendMessage(chat_id=791147649, text="马拉开波448有货")
#        print bot.getMe()
#        print('\033[0m')
        