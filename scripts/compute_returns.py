# -*- coding: utf-8 -*-

from datetime import datetime
from bson.objectid import ObjectId
from pymongo import DESCENDING

from fund.db import DB
from fund.settings import (
    MONGO,
    NEXT_DAY,
    MONTHS, SINCE_INCEPTION,
)

def get_value(collection, date, direction=0, field='price', iteration=1):
    value = collection.find_one({'_id': ObjectId.from_datetime(date)})
    if not value:
        next_iteration = 0
        if direction == 0:
            if iteration > 0:
                next_iteration = (iteration + 1) * -1
            else:
                next_iteration = (iteration - 1) * -1
        elif direction == 1:
            next_iteration = iteration + 1
        elif direction == -1:
            next_iteration = iteration - 1

        try:
            return get_value(collection, date + (NEXT_DAY * iteration), direction, \
                field, next_iteration)
        except RuntimeError:
            print 'ERROR: Collection %s (%d/%d/%d, iteration %d)' % (collection.name, \
                date.day, date.month, date.year, iteration)
            return -1.0

    return value[field]

def absolute_return(start, end):
    if start:
        return (100 * (end - start)) / start
    return 'inf'

# pylint: disable-msg=too-many-locals
def compute_returns():
    funds = DB[MONGO['collection']]

    fund_list = DB.collection_names(include_system_collections=False)
    fund_list.remove(MONGO['collection'])

    for fund in fund_list:
        collection = DB[fund]

        latest = collection.find().sort('date', DESCENDING).limit(1)[0]['date']

        fund_record = funds.find_one({'code': fund})
        earliest = fund_record['start_date']
        # time_period = (latest - earliest).days

        latest_price = collection.find_one({'date': latest})['price']
        for name, value in MONTHS.iteritems():
            month = latest - value
            if month > earliest:
                price_then = get_value(collection, month)
                fund_record[name] = absolute_return(price_then, latest_price)

        earliest_price = collection.find_one({'date': earliest})['price']
        fund_record[SINCE_INCEPTION] = absolute_return(earliest_price, latest_price)

        latest_year = latest.year
        years = latest_year - earliest.year

        price_then = get_value(collection, datetime(latest_year, 1, 1, 0, 0, 0))
        fund_record[str(latest_year)] = absolute_return(price_then, latest_price)

        for i in range(1, years):
            year = latest_year - i
            price_now = get_value(collection, datetime(year, 12, 31, 0, 0, 0))
            price_then = get_value(collection, datetime(year, 1, 1, 0, 0, 0))
            fund_record[str(year)] = absolute_return(price_then, price_now)

        year = latest_year - years
        price_now = get_value(collection, datetime(year, 12, 31, 0, 0, 0))
        fund_record[str(year)] = absolute_return(earliest_price, price_now)

        funds.save(fund_record, manipulate=True)

if __name__ == '__main__':
    compute_returns()
