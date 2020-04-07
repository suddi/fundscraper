# pylint: disable-msg=line-too-long
from configparser import ConfigParser
from datetime import timedelta
from dateutil.relativedelta import relativedelta

credentials = ConfigParser()
credentials.read('credentials.ini')

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 10

SPIDER_MODULES = ['fund.spiders']
NEWSPIDER_MODULE = 'fund.spiders'

MONGO = {
    'host': credentials.get('DEFAULT', 'MONGO_HOST') or 'mongodb://localhost:27017',
    'database': 'scrapedb',
    'collection': 'funds',
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'fund.middleware.useragent.RandomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
    'fund.pipelines.storage.StoragePipeline': 700,
}

FUND_LIST_URL = 'http://www.aia.com.hk/en/investment-information/fund_hist_content_new.jsp'
FUND_PRICE_URL = 'http://www.aia.com.hk/en/investment-information/fund_search_content_new.jsp?fund=%s&tier=%s&date=%s&todate=%s'
FUNDS = 'funds.json'
FUND_LIST = []

ACTION = {
    'COMPILE_FUNDS': 0,
    'GET_PRICES': 1,
}
TAKE_ACTION = ACTION['GET_PRICES']

NEXT_DAY = timedelta(days=1)
PREVIOUS_DAY = timedelta(days=-1)

MONTHS = {
    '3 months'   : relativedelta(months=3),
    '6 months'   : relativedelta(months=6),
    '9 months'   : relativedelta(months=9),
    '12 months'  : relativedelta(months=12),
    '24 months'  : relativedelta(months=24),
    '60 months'  : relativedelta(months=60),
    '120 months' : relativedelta(months=120),
    '180 months' : relativedelta(months=180),
    '240 months' : relativedelta(months=240),
}

SINCE_INCEPTION = 'since_inception'

WEIGHTING = {
    '6 months'   : 5.0,
    '12 months'  : 10.0,
    '24 months'  : 7.0,
    '60 months'  : 2.0,
    '120 months' : 1.0,
}
