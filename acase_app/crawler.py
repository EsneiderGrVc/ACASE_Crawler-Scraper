import os
from selenium import webdriver
from acase_app.consts import driver_dir
from acase_app.scraper import Scraper

class Crawler(webdriver.Chrome):
    def __init__(self, driver_path=driver_dir, teardown=False):
        # Driver path is required for Selenium to execute the brower driver
        self.driver_path = driver_path

        # Teardown indicates to the program if it must closed the window browser
        # Once the script is ended or let it open.
        self.teardown = teardown

        # The OS PATH takes the driver_path to concatenate, then Selenium executes it
        os.environ['PATH'] += self.driver_path

        # The Super method brings to Crawler class some attributes given in
        # webdriver class,  like Session_id for instance.
        super(Crawler, self).__init__()

    def start(self, url):
        self.get(url)

    def __exit__(self, *args):
        if self.teardown:
            super().__exit__(*args)

    def ads_breaker(self):
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)
        identifier = soup.bs4()
        print(f'This is the identifier: {identifier}')
        close_btn = self.find_element_by_id(identifier)
        close_btn.click()

