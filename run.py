import time
from acase_app.crawler import Crawler
from acase_app.consts import target
from acase_app.scraper import Scraper

# with open('hrt', 'r') as mercer:
    # scraper = Scraper()
    # scraper.find_input()

keywords = 'liderazgo'
# for _, url in target.items():
    # with Crawler(teardown=True, keywords=keywords) as bot:
        # bot.start(url)
        # bot.ads_breaker()
        # bot.enable_search()
        # bot.perform_search()
        # bot.extract_results()

farming = []

with Crawler(url=target.get('deloitte'), teardown=True, keywords=keywords) as bot:
    bot.start()
    bot.ads_breaker()
    bot.enable_search()
    bot.perform_search()
    results = bot.extract_results()
    print(f'Results: {results}')
    # for result in results:
        # farming.append(result)

# print(farming)
# print(f'\n:: Se han minado {len(farming)} recursos ::')
