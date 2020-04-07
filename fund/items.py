from scrapy.item import Field, Item

# pylint: disable-msg=too-many-ancestors
class FundItem(Item):
    code = Field()
    name = Field()
    tier = Field()
    start_date = Field()

    date = Field()
    price = Field()
