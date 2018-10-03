import scrapy

class MushroomWorldItem(scrapy.Item):
    name = scrapy.Field()
    family = scrapy.Field()
    location = scrapy.Field()
    dimensions = scrapy.Field()
    edibility = scrapy.Field()
    description = scrapy.Field()
