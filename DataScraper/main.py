from bs4 import BeautifulSoup
import requests
from typing import List
from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager

HEADERS: dict[str, str] = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
PAGES: int = 2


if __name__ == "__main__":
    DATA_FILE = "../player_data.csv"
    
    FileManager.Manager().clear_file(DATA_FILE)
    with open(DATA_FILE, 'a', encoding="utf-8") as file:
        file.write('Rank, IGN, Tier, LP, Win-Lose, Winrate, Most Played, KDA, Avg CS, KP, \n')

        for i in range(PAGES + 1):
            url = f"https://www.op.gg/leaderboards/tier?region=euw&page={i}"

            try:
                resp = requests.get(url, headers=HEADERS, timeout=60)
            except requests.exceptions.ConnectionError as e:
                pass
            soup = BeautifulSoup(resp.content, "lxml")

            for i in ProfileScraper.Scraper(soup).scrape_profiles():
                Analyzer = Profile_Analyzer('https://op.gg' + i)
                file.write(Analyzer.get_data())
# TODO:
#   Implement for all regions
#   Search on conditions(wr, champ, rank, )