import requests
from bs4 import BeautifulSoup

class CoronaService:
    def __init__(self):
        self.base_url = 'https://www.worldometers.info/coronavirus/'

    def get_info(self, country=None):
        try:
            url = self.base_url
            if country:
                url += f'country/{country}/'

            response = requests.get(url)
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