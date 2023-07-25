import scrapy
from itemloaders.processors import TakeFirst, MapCompose
# TakeFirst is processor used to extract first value from a list of values
# MapCompose is used to apply list of functions to value, chaining functions together in a single step.
# MapCompose allows us to define a pipeline of processing steps that will be applied to each field in item
# as value is extracted from selector and then load it onto the item
from w3lib.html import remove_tags

# functions for post-processing of values
def remove_commas(value):
    return value.replace(',', '')


def try_float(value):
    try:
        return float(value)
    except ValueError:
        return value


def try_int(value):
    try:
        return int(value.split(']')[-1])
    except ValueError:
        return value


class CountriesGdpItem(scrapy.Item):
    # define the fields for your item here like:
    country_name = scrapy.Field(
        # what goes into field (html)
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()    # what comes out and is assigned
    )
    region = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    gdp = scrapy.Field(
        input_processor=MapCompose(
            remove_tags, str.strip, remove_commas, try_float),
        output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, try_int),
        output_processor=TakeFirst()
    )
