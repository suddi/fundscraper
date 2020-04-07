from pymongo import MongoClient

from scrapy.conf import settings

def establish_connection():
    connection = MongoClient(settings.get('MONGO', {})['host'])
    database = connection[settings.get('MONGO', {})['database']]

    return database

DB = establish_connection()
