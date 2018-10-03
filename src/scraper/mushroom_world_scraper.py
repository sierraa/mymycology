from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from mushroom_world_item import MushroomWorldItem

class MushroomWorldSpider(CrawlSpider):
    name = "mushroom_world_spider"
    start_urls = ["http://www.mushroom.world/mushrooms/namelist"]

    rules = (
        Rule(LxmlLinkExtractor(
            restrict_xpaths=("//div[@class='item']")),
            follow=True,
            callback='parse_item'
        ),
      )

    def parse_item(self, response):
        name = response.css(".caption ::text")
        description = response.css(".longtextus ::text")
        family = response.css(".textus:nth-child(0) ::text")
        location = response.css(".textus:nth-child(1) ::text")
        dimensions = response.css(".textus:nth-child(2) ::text")
        edibility = response.css(".textus:nth-child(3) ::text")
        yield MushroomWorldItem(name=name, description=description, family=family,
                                    location=location, dimensions=dimensions, edibility=edibility)
