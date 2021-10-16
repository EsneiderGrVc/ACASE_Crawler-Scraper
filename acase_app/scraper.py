from bs4 import BeautifulSoup
from re import search

class Scraper():
    def __init__(self, html_element):
        self.soup = BeautifulSoup(html_element, 'html.parser')
        # uncomment to save the entire html object and
        # execute this program without open the browser

        # with open('hrt', 'w') as f:
            # f.write(self.soup.prettify())

    def find_ads(self):
        element_target = {'a': [], 'button': []}
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
                    for button in div.find_all('button'):
                        for key, attr in button.attrs.items():
                            if search('close', str(attr).lower()):
                                element_target['button'].append({str(key): attr})
        return element_target



    def find_search_field(self):
        inputs = self.soup.find_all('input')
        target = []

        for input_elem in inputs:
            for attr, value in input_elem.attrs.items():
                if str(attr) == 'placeholder' and search('search', str(value).lower()):
                    target.append({attr: value})
                if str(attr) == 'placeholder' and search('buscar', str(value).lower()):
                    target.append({attr: value})

        return target


    def find_search_enable_btn(self):
        """ This method returns for the 'attr=value'
        of the element that once clicked allows write
        in the placeholder"""

        target = {
            'span':  [],
            'button': [],
            'a': []
        }

        for tag in target.keys():
            elems = self.soup.find_all(str(tag))
            for btn in elems:
                for attr, value in btn.attrs.items():
                    if search('search', str(value).lower()):
                        target[tag].append({attr: value})
                if len(target[tag]) > 0:
                    return target
