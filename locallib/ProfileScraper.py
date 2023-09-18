from typing import List

class Scraper:
    def __init__(self, soup) -> None:
        self.soup = soup
    def scrape_profiles(self) -> List[str]:
        try:
            profiles: List[str] = self.soup.find_all('tr', {"class" : "css-3phihe e1r55j540"})
        except AttributeError as e:
            print(e)
        except TypeError as e:
            print(e)
        links: List[str] = []
        for profile in profiles:
            link: str = profile.find('a').get('href')
            links.append(link)
        return links