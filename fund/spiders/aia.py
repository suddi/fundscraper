# -*- coding: utf-8 -*-

from re import findall
from datetime import date
from dateutil.relativedelta import relativedelta
from pymongo import DESCENDING

from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings

from fund.db import DB
from fund.items import FundItem
from fund.loader.itemloader import FundItemLoader

class FundSpider(CrawlSpider):
    name = 'aia.com.hk'
    url = 'http://www.aia.com.hk/'
    allowed_domains = ['aia.com.hk',]

    def __init__(self, *args, **kwargs):
        super(FundSpider, self).__init__(*args, **kwargs)
        self.data = {}

    def start_requests(self):
        if settings['TAKE_ACTION'] == settings.get('ACTION', {})['COMPILE_FUNDS']:
            # Create an initial JSON file which compiles a list of the available
            # funds with the names, codes, tier and start date.
            yield Request(settings['FUND_LIST_URL'], callback=self.parse_list)

        elif settings['TAKE_ACTION'] == settings.get('ACTION', {})['GET_PRICES']:
            collection = DB[settings.get('MONGO', {})['collection']]
            cursor = list()
            if settings['FUND_LIST']:
                for fund in list(settings['FUND_LIST']):
                    cursor.append(collection.find_one({'code': fund}))
            else:
                cursor = collection.find()

            today = date.today()
            for item in cursor:
                if item['code'] in DB.collection_names():
                    start_date = DB[item['code']] \
                        .find() \
                        .sort('date', DESCENDING) \
                        .limit(1)[0]['date']
                else:
                    start_date = item['start_date']

                diff = relativedelta(today, start_date)
                if not diff.years and not diff.months and not diff.days:
                    occurences = 0
                else:
                    occurences = ((diff.years * 12 + diff.months) / 3) + 1
                for i in range(0, occurences):
                    new_date = start_date + relativedelta(months=(i * 3))
                    new_date = new_date.strftime('%m/%d/%Y')
                    yield Request(settings['FUND_PRICE_URL'] % (item['code'], item['tier'], \
                        new_date, '3m'), callback=self.parse_price, meta={'code': item['code']})

    # Only to be used when forming the initial JSON file, which compiles a
    # list of the available funds with the names, codes, tier and start date.
    def parse_list(self, response):
        hrefs = response.xpath('//table[2]//tr[descendant::a]')

        for href in hrefs:
            name = href.xpath('./td/a/text()').extract()[0].strip()
            code = href.xpath('./td[2]/text()').extract()[0]
            code = findall(r'[\w\d]+', code)[0].strip()
            tier = href.xpath('./td/a/@onclick').extract()[0]
            tier = findall(r'&tier=([\w+_]+)&', tier)[0].strip()

            self.data[code] = {'name': name, 'tier': tier}

            yield Request(settings['FUND_PRICE_URL'] % (code, tier, '', ''),
                          callback=self.parse_fund, meta={'code': code})

    # Uses the initial JSON file to get the starting dates of the
    # respective funds.
    def parse_fund(self, response):
        code = response.meta['code']

        item = FundItemLoader(FundItem(), response=response)
        item.add_value('code', code)
        item.add_value('name', self.data[code]['name'])
        item.add_value('tier', self.data[code]['tier'])
        item.add_xpath('start_date', '//u/text()')

        yield item.load_item()

    def parse_price(self, response):
        hrefs = response.xpath('//td[text()="Valuation Date"]//ancestor::table//tr')

        for href in hrefs:
            item = FundItemLoader(FundItem(), response=response)

            item.add_value('code', response.meta['code'])
            bid_date = href.xpath('./td[1]/text()').extract()
            item.add_value('date', bid_date)
            price = href.xpath('./td[2]/text()').extract()
            item.add_value('price', price)

            yield item.load_item()
