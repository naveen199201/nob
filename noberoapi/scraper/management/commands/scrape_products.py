from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from django.core.management.base import BaseCommand
from nobero.spiders.men_page_spider import MenPageSpider

class Command(BaseCommand):
    help = 'Run the MensSpider Scrapy spider'

    def handle(self, *args, **kwargs):
        process = CrawlerProcess(get_project_settings())
        process.crawl(MenPageSpider)
        process.start()
