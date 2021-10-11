from bs4 import BeautifulSoup
from re import search

class Scraper():
    def __init__(self, html_element):
        self.soup = BeautifulSoup(html_element, 'html.parser')

    def bs4(self):
        # Get all divs elements from a website
        divs = self.soup.find_all('div')

        # Iterate each div element
        for div in divs:
            # Iterate the attributes that contains each div tag
            for attribute in div.attrs.values():
                # Searching for 'modal' word in each attribute
                if search('modal', str(attribute)):
                    return div.find('a').attrs.get('id')
                # if type(atr) == list:
                    # for elem in atr:
                        # if search('modal', elem):
                            # print('Bingo!!!')
                            # print(f'número de divs: {count}')
                            # return

    def encap(self, html_element):
        soup = BeautifulSoup(html_element, 'html.parser')
        return soup
