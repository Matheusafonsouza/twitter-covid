import requests
from bs4 import BeautifulSoup

class CoronaService:
    def __init__(self):
        self.url = 'https://www.worldometers.info/coronavirus/country/brazil/'

    def get_info(self):
        try:
            response = requests.get(self.url)
        except Exception:
            raise Exception('Something gone bad on corona request')

        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.findAll('div', { "class": "maincounter-number" })

        if not container or len(container) < 1:
            raise Exception('Corona scrapper return nothing :(')

        return dict(
            cases=self.format_counter(container[0]),
            deaths=self.format_counter(container[1]),
            recovered=self.format_counter(container[2])
        )

    def format_counter(self, container):
        counter = container.text
        if not counter:
            return '0'
        return counter.strip()