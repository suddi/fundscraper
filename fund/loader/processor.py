# -*- coding: utf-8 -*-

from re import findall
from datetime import datetime

def normalize_string(value, separator=' '):
    if isinstance(value, basestring):
        value = unicode(value)
        return separator.join(value.split())
    return value

def format_string(value):
    return value.replace("'", "''").replace('"', '""')

def extract_int(value):
    def extract_int_from_float(value):
        try:
            return int(extract_float(value))
        except TypeError:
            return None

    if isinstance(value, int):
        return value
    elif isinstance(value, float):
        return int(round(value))
    elif isinstance(value, basestring):
        return extract_int_from_float(value)
    return None

def extract_float(value):
    if isinstance(value, float):
        return value
    elif isinstance(value, int):
        return float(value)
    elif isinstance(value, basestring):
        value_match = findall(r'[\d\.\,]+', value)
        if value_match:
            value = value_match[0].replace(',', '')
            return float(value)
    return None

# pylint: disable-msg=broad-except
def cast_datetime(value):
    if isinstance(value, basestring):
        try:
            return datetime.strptime(value, '%m/%d/%Y')
        except Exception:
            try:
                return datetime.strptime(value, '%m-%d-%Y')
            except ValueError:
                return None
