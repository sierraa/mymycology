import scrapy

class MushroomWorldSpider(scraper.Spider):
    name = "mushroom_world_spider"
    start_urls = ["http://www.mushroom.world/mushrooms/namelist"]
