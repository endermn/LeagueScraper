from bs4 import BeautifulSoup
import requests
from typing import List
from time import sleep
from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager

HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
PAGES = 1

FileManager.Manager().clear_file('data.csv')

file = open('data.csv', 'a', encoding="utf-8")

for i in range(PAGES + 1):
    url = f"https://www.op.gg/leaderboards/tier?region=euw&page={i}"

    try:
        resp = requests.get(url, headers=HEADERS, timeout=60)
    except requests.exceptions.ConnectionError as e:
        pass
    soup = BeautifulSoup(resp.content, "lxml")

    for i in ProfileScraper.Scraper(soup).scrape_profiles():
        Analyzer = Profile_Analyzer('https://u.gg/lol' + i + "/overview")
        file.write(Analyzer.get_data())

# TODO:
#   Implement for all regions
