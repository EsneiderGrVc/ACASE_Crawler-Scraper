from bs4 import BeautifulSoup
from re import search

class Scraper():
    def __init__(self, html_element):
        self.soup = BeautifulSoup(html_element, 'html.parser')
        # uncomment to save the entire html object and
        # execute this program without open the browser

        # with open('hrt', 'w') as f:
            # f.write(self.soup.text)

    def find_ads(self):
        element_target = {
            "a": []
        }
        # Get all divs elements from a website
        divs = self.soup.find_all('div')
        # Iterate each div element
        for div in divs:
            # Iterate the attributes that contains each div tag
            for attribute in div.attrs.values():
                # Searching for 'modal' word in each attribute
                if search('modal', str(attribute)):
                    for anchor in div.find_all('a'):
                        for key, attr in anchor.attrs.items():
                            if search('close', str(attr).lower()):
                                element_target['a'].append({str(key): attr})
                                # print(f'{key}: {attr}')
                    # return div.find('a').attrs.get('id')
        return element_target
