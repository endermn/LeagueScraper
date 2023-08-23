from typing import List

class Scraper:
    def __init__(self, soup) -> None:
        self.soup = soup
    def scrape_profiles(self) -> List[str]:
        profiles = self.soup.find_all('tr', {"class" : "css-3phihe e1r55j540"})
        links: List[str] = []
        for i in profiles:
            link = i.find('a').get('href')
            link = link.replace('summoners', 'profile')
            link = link.replace('euw', 'euw1')
            links.append(link)
        return links