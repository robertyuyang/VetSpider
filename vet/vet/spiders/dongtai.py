# -*- coding: utf-8 -*-
import scrapy
import re
from vet.items import VetItem
from scrapy.http import Request

class DongtaiSpider(scrapy.Spider):
    name = 'dongtai'
    allowed_domains = ['www.syj.moa.gov.cn']
    #start_urls = ['http://www.syj.moa.gov.cn/dongtai/./201806/t20180622_6152903.htm']
    start_urls = ['http://www.syj.moa.gov.cn/dongtai/']
    url_set = set()

    print 'start'

    def parse(self, response):
        #print '+++parse'
        #print response.url

        if response.url.startswith("http://www.syj.moa.gov.cn/dongtai/./"):
            title_ele = response.xpath('//div[@class="article_bt"]')
            title = title_ele.xpath('string(.)').extract()[0].encode('utf-8')
            value = ''
            spans = response.xpath("//span")
            for span in spans:
                t = span.xpath('string(.)').extract()[0].encode('utf-8')
                #print 't2:'+str(t)
                text = str(t)
                result =re.findall('(白条肉平均出厂价格为((.+)元/公斤))', text)
                if len(result) == 1 :
                    value = result[0][0]
                    break

            print  title + ' '+ value
            #print 'zzzzz'
            #title = response.xpath('//div[@class="article_bt"]/text()')[0].encode('utf-8')
            #print 'title:====='+title

            pass
        if response.url.startswith("http://www.syj.moa.gov.cn/dongtai/index_"):
            nodes = response.xpath('//ul[@class="zj_list"]/li')
            for node in nodes:
                item = VetItem()
                report_name =  node.xpath('./a/@title').extract()[0].encode('utf-8')
                #print 'report_name:'
                #print report_name
                #print typeof(report_name)
                if report_name.startswith('一周兽医要闻纵') and report_name.endswith('（国内版）'):
                    report_url = node.xpath('./a/@href').extract()[0].encode('utf-8')
                    report_url = 'http://www.syj.moa.gov.cn/dongtai/' + report_url
                    #print report_name + '---' + report_url
                    #yield Request(report_url, callback=self.parse)
                    # yield self.make_requests_from_url(report_url)
                    # item['report_name'] = report_name
                    # yield item


                    if report_url in DongtaiSpider.url_set:
                        continue
                    else:
                        DongtaiSpider.url_set.add(report_url)
                        # 回调函数默认为parse,也可以通过from scrapy.http import Request来指定回调函数
                        # from scrapy.http import Request
                        # Request(url,callback=self.parse)
                        yield self.make_requests_from_url(report_url)



        for i in range(1, 50):
            url = 'http://www.syj.moa.gov.cn/dongtai/index_' + str(i) +'.htm'

            if url in DongtaiSpider.url_set:
               continue
            else:
                DongtaiSpider.url_set.add(url)
                    # 回调函数默认为parse,也可以通过from scrapy.http import Request来指定回调函数
                    # from scrapy.http import Request
                    # Request(url,callback=self.parse)
                yield self.make_requests_from_url(url)
