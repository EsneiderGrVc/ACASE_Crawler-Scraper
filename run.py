from acase_app.crawler import Crawler
from acase_app.consts import target
from acase_app.scraper import Scraper

# with open('mercer', 'r') as mercer:
    # scraper = Scraper(mercer)
    # scraper.find_ads()

with Crawler() as bot:
    bot.start(target.get('mercer'))
    bot.ads_breaker()
