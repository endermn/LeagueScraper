from bs4 import BeautifulSoup
import requests


class Patch():
    def __init__(self, url: str, headers: dict[str, str]) -> None:
        self.url = url
        self.headers = headers
    def scrape_patch(self) -> str:
        try:
            resp = requests.get(self.url, headers=self.headers, timeout=60)
        except requests.exceptions.ConnectionError:
            pass
        soup = BeautifulSoup(resp.content, "lxml")
        
        patch = soup.find('h2', {'data-testid' : 'articlelist:article-0:title'}).text.strip()
        
        return patch
