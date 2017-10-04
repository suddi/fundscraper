# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

from scrapy.conf import settings

from fund.db import DB

class StoragePipeline(object):
    def process_item(self, item):
        if settings['TAKE_ACTION'] == settings.get('ACTION', {})['COMPILE_FUNDS']:
            collection = DB[settings.get('MONGO', {})['collection']]

            existing_record = collection.find_one({'code': item['code']})
            if not existing_record:
                collection.save(dict(item))

        elif settings['TAKE_ACTION'] == settings.get('ACTION', {})['GET_PRICES']:
            collection = DB[item['code']]

            if 'date' in item:
                collection.save({
                    '_id': ObjectId.from_datetime(item['date']),
                    'date': item['date'], 'price': item['price']
                }, manipulate=True)

        return item
