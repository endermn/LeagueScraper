from bs4 import BeautifulSoup
import requests
from typing import Dict


def scrape_patch(url: str, headers: Dict[str, str]) -> str:
    try:
        resp = requests.get(url, headers=headers, timeout=60)
    except requests.exceptions.ConnectionError:
        pass
    soup = BeautifulSoup(resp.content, "lxml")
    
    patch = soup.find('h2', {'data-testid' : 'articlelist:article-0:title'}).text.strip()
    
    return patch
