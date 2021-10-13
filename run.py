from acase_app.crawler import Crawler
from acase_app.consts import target
from acase_app.scraper import Scraper

# with open('hrt', 'r') as mercer:
    # scraper = Scraper(mercer)
    # scraper.find_ads()

with Crawler(teardown=True) as bot:
    bot.start(target.get('hrt'))
    bot.ads_breaker()
    bot.link_visitor()
