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
        name = response.css(".caption b ::text").extract_first().strip()
        description = response.css(".longtextus ::text").extract_first()
        family = response.css(".textus ::text").extract_first()
        location = response.xpath(".//textus[1]/text()").extract()
        dimensions = response.css("#mushroom-list:nth-child(2) ::text").extract()
        edibility = response.css("#mushroom-list:nth-child(3) ::text").extract()
        yield MushroomWorldItem(name=name, description=description, family=family,
                                    location=location, dimensions=dimensions, edibility=edibility)
