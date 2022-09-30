from collections import defaultdict

class Emissions:
    def __init__(self):
        # e.g. data = { country: [value_1980, value_2018] }
        self.data = defaultdict(list)

    def add(self, country, value):
        self.data[country].append(value)
    
    def get_top_ten_countries(self):
        sorted_data = sorted(
            self.data.items(), 
            key=lambda d: d[1][1], 
            reverse=True)
        return [d[0] for d in sorted_data[:10]]

    def get_difference(self):
        difference = {}
        for country in self.data:
            [value_1980, value_2018] = self.data[country]
            difference[country] = value_2018 - value_1980
        return difference

class WebScrapper:
    def __init__(self):
        self.emissions = Emissions()

    def _scrape_mock_data(self):
        mock_data = {
            'Afganistan': [0.1, 0.3],
            'Albania': [1.9, 1.6],
            'Algeria': [3.4, 3.9],
            'Egypt': [1.0, 2.5],
            'France': [9.1, 5.0]
        }
        for country in mock_data:
            [value_1980, value_2018] = mock_data[country]
            self.emissions.add(country, value_1980)
            self.emissions.add(country, value_2018)
    
    def scrape_data(self):
        # TODO: scrape data from wikipedia
        # self.emissions.add(country, value_1980)
        # self.emissions.add(country, value_2018)
        self._scrape_mock_data()
    
    def print_results(self):
        top_ten_countries = self.emissions.get_top_ten_countries()
        print(f'top_ten_countries={top_ten_countries}')
        difference = self.emissions.get_difference()
        print(f'difference={difference}')
        


if __name__ == '__main__':
    web_scraper = WebScrapper()
    web_scraper.scrape_data()
    web_scraper.print_results()