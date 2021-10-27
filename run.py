import time
import pdb
import json
from termcolor import colored
from acase_app.crawler import Crawler
from acase_app.consts import target
from acase_app.scraper import Scraper

def run_bot(target):

    farming = []

    if type(target) is not list:
        print('Please insert a list of objects')
    else:
        for resource in target:
            if len(resource.get('keywords')) == 0:
                continue
            for keyword in resource.get('keywords'):
                try:
                    with Crawler(url=resource.get('url'), teardown=True, keywords=keyword) as bot:
                        bot.start()
                        bot.ads_breaker()
                        bot.enable_search()
                        bot.perform_search()
                        results = bot.extract_results() # [{}, {}, {}]
                    for result in results:
                        farming.append(result)
                except Exception as err:
                    print(err)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(farming, f)


def scan_results():
    with open('results.json', 'r') as f:
        results = json.load(f)
        for item in results:
            if not 'Url' in item:
                item['Url'] = ':: suspicious item ::'
                for key, value in item.items():
                    print(colored(f'{key}: ', 'green'), end='')
                    print(value)
                print('-'*50)
                print('-'*50)

if __name__ == '__main__':
    run_bot(target)
    scan_results()
