
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict

def format(val):
    return float('{:.1f}'.format(val))
class Emissions:
    def __init__(self):
        # e.g. data = { country: [value_1980, ..., value_2018] }
        self.data = defaultdict(list)

    def add(self, country, value):
        self.data[country].append(value)
    
    def get_top_ten_countries(self):
        sorted_data = sorted(
            self.data.items(), 
            key=lambda d: d[1][-1], 
            reverse=True)
        result = []
        for d in sorted_data[:10]:
            result_list = [
                d[1][0],
                d[1][-1],
                format(d[1][-1] - d[1][0]),
            ]
            result.append((d[0], result_list))
        return result

class WebScrapper:
    def __init__(self):
        self.emissions = Emissions()
    
    def scrape_data(self):
        # scrape data from wikipedia
        url = 'https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita'
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.select('table')[1]
        for tbody in table.find_all('tbody'):
            for tr in tbody.find_all('tr')[1:]:
                row = str(tr.text.strip())
                split_row = row.split('\n')
                country = split_row[0]
                for val in split_row[1:]:
                    val = val.replace('..', '0')
                    number = float(val)
                    self.emissions.add(country, number)
    
    def print_results(self):
        top_ten_countries = self.emissions.get_top_ten_countries()
        print(f'top_ten_countries={top_ten_countries}')
        


if __name__ == '__main__':
    web_scraper = WebScrapper()
    web_scraper.scrape_data()
    web_scraper.print_results()