import os
import time
from selenium import webdriver
from acase_app.consts import driver_dir
from acase_app.scraper import Scraper

class Crawler(webdriver.Chrome):
    def __init__(self, driver_path=driver_dir, teardown=False):
        # Driver path is required for Selenium to execute the brower driver
        self.driver_path = driver_path

        # Teardown indicates to the program if it must to close the window browser
        # Once the script is ended or let it open.
        self.teardown = teardown

        # The OS PATH takes the driver_path to concatenate it, then Selenium executes it
        os.environ['PATH'] += self.driver_path

        # The Super method brings to Crawler class some attributes given in
        # webdriver class,  like Session_id for instance.
        super(Crawler, self).__init__()

    def start(self, url):
        """ Open the browser with a given url"""
        self.get(url)

    def __exit__(self, *args):
        """Close the browser application if teardown
        is True once the program is done"""
        if self.teardown:
            super().__exit__(*args)

    def ads_breaker(self):
        """ This method searching for the body html element,
        sends it to the Scraper class to find potencials pop-ups
        and finally close them"""
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)
        target_element = soup.find_ads()

        for tag, keyattr_list in target_element.items():
            for keyattr in keyattr_list:
                for key, attr in keyattr.items():
                    try:
                        self.find_element_by_css_selector(
                            f'{tag}[{key}="{attr}"]'
                        ).click()
                        print('Element clicked!')
                    except:
                        print('The element was clicked or something went wrong')
        # print(count)
        # print(f'This is the identifier: {identifier}')
        # close_btn = self.find_element_by_id(identifier)
        # close_btn.click()

    def link_visitor(self):
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        print(html_element)
        soup = Scraper(html_element)
        links = soup.get_links()
        for elem in links:
            print(elem)
        print(type(links))


