from bs4 import BeautifulSoup
import requests
from typing import List
from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager
import most_frequent

HEADERS: dict[str, str] = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
PAGES: int = 1

def write_data(data_file) -> None:
    FileManager.Manager(data_file).clear_file()
    with open(data_file, 'a', encoding="utf-8") as file:
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
    
    most_frequent.Most_Frequent_Values().write_data()

def main() -> None:
    DATA_FILE: str = "../player_data.csv"
    write_data(DATA_FILE)

if __name__ == "__main__":
    main()
# TODO:
#   Search on conditions(wr, champ, rank, )
#   Update on new Patch only