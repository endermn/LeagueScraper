from typing import List
import logger

ProfileLogger = logger.setup_logging("ProfileLogger", False)
class Scraper:
    def __init__(self, soup) -> None:
        self.soup = soup
        try:
            self.profiles: List[str] = self.soup.find_all('tr', {"class" : "css-3phihe e1r55j540"})
        except AttributeError as e:
            ProfileLogger.exception("AttributeError")
        except TypeError as e:
            ProfileLogger.exception("TypeError")
    def scrape_profiles(self) -> List[str]:
        links: List[str] = []
        for profile in self.profiles:
            link: str = profile.find('a').get('href')
            links.append(link)
        return links