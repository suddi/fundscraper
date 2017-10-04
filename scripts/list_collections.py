# -*- coding: utf-8 -*-

from fund.db import DB

def list_collections():
    collection_list = DB.collection_names(include_system_collections=False)

    map(print_value, collection_list)

def print_value(value):
    print value

if __name__ == '__main__':
    list_collections()
