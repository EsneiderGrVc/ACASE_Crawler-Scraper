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
                print('no hay keywords')
                continue
            for keyword in resource.get('keywords'):
                print(colored(f'Scraping {keyword} from {resource.get("name")}...', 'blue'))
                with Crawler(url=resource.get('url'), teardown=True, keywords=keyword) as bot:
                    bot.start()
                    bot.ads_breaker()
                    bot.enable_search()
                    bot.perform_search()
                    results = bot.extract_results() # [{}, {}, {}]
                    # print(f'{len(results)} from {keyword}: {resource.get("name")}')
                    try:
                        for result in results:
                            farming.append(result)
                    except Exception as err:
                        print(err)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(farming, f)

def scan_results():
    with open('results.json', 'r') as f:
        results = json.load(f)
        for count, item in enumerate(results):
            if not 'Url' in item:
                item['Url'] = ':: suspicious item ::'
                for key, value in item.items():
                    print(colored(f'{key}: ', 'green'), end='')
                    print(value)
                print('-'*50)
                print('-'*50)
            if count + 1 == len(results):
                print(count + 1)

def parse_frontend_json():
    """This function perform a JSON file usable for the frontend"""
    with open('results.json', 'r') as f:
        results = json.load(f)
        count = 0
        for item in results:
            count += 1
            item['Id'] = count
            item['My_selection'] = False
            item['Trash_section'] = False
            item['Relevance'] = ''
            item['Learning'] = ''
            item['Finding'] = ''
            item['Page'] = ''
            if not 'Url' in item:
                item['Url'] = ':: suspicious item ::'
                for key, value in item.items():
                    print(colored(f'{key}: ', 'green'), end='')
                    print(value)
                print('-'*50)
                print('-'*50)

        with open('new_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f)
        with open('new_results.json', 'r', encoding='utf-8') as o:
            print(json.load(o))

if __name__ == '__main__':
    run_bot(target)
    scan_results()
