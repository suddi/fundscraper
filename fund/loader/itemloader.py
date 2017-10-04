# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from fund.loader.processor import (
    normalize_string, format_string,
    extract_float,
    cast_datetime,
)

class FundItemLoader(ItemLoader):
    def __init__(self, *args, **kwargs):
        super(FundItemLoader, self).__init__(*args, **kwargs)

        self.default_input_processor = MapCompose(normalize_string, format_string)
        self.default_output_processor = TakeFirst()

        self.start_date_in = MapCompose(cast_datetime)

        self.date_in = MapCompose(cast_datetime)
        self.price_in = MapCompose(extract_float)
