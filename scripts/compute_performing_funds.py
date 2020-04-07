from pymongo import DESCENDING

from fund.settings import MONGO, WEIGHTING
from fund.db import DB

def compute_performing_funds():
    funds = DB[MONGO['collection']]

    funds_list = funds.find()
    for fund in funds_list:
        performance = 0

        for key, weight in WEIGHTING.items():
            performance += fund.get(key, 0.0) * weight
        fund['performance'] = performance

        funds.save(fund, manipulate=True)

    top = funds.find().sort('performance', DESCENDING).limit(20)
    for count, fund in enumerate(top):
        print('Number %d: %s (%f)' % (count, fund['code'], fund['performance']))

if __name__ == '__main__':
    compute_performing_funds()
