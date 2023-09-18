from bs4 import BeautifulSoup
import requests
from typing import List
from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager
import most_frequent
import PatchScraper
import tkinter as tk
from tkinter import Button
from tkinter import messagebox as mb

HEADERS: dict[str, str] = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

PAGES: int = 1

def call() -> bool:
    res=mb.askquestion('Refresh data', 'Do you really want to refresh the data')
    if res == "yes":
        return True
    return False

def write_data(data_file: str, patch: str) -> None:
    FileManager.Manager(data_file).clear_file()
    with open(data_file, 'a', encoding="utf-8") as file:
        file.write('Rank, IGN, Tier, LP, Win-Lose, Winrate, Most Played, KDA, Avg CS, KP, \n')

        for i in range(1, PAGES + 1):
            url: str = f"https://www.op.gg/leaderboards/tier?region=euw&page={i}"

            try:
                resp = requests.get(url, headers=HEADERS, timeout=60)
            except requests.exceptions.ConnectionError:
                pass
            soup = BeautifulSoup(resp.content, "lxml")
            profiles: List[str] = ProfileScraper.Scraper(soup).scrape_profiles()
            
            for i in range(5):
                Analyzer = Profile_Analyzer('https://op.gg' + profiles[i])
                file.write(Analyzer.get_data())
    
    most_frequent.Most_Frequent_Values().write_data(patch)



def main() -> None:
    DATA_FILE: str = "../player_data.csv"
    Patch = PatchScraper.Patch("https://www.leagueoflegends.com/en-us/news/tags/patch-notes/", HEADERS)
    CURRENT_PATCH = Patch.scrape_patch()
    first_line: str = ""
    
    with open('../average_stats.csv', 'r', encoding='utf-8') as file:
        first_line = file.readline()

    first_line = ''.join(c for c in first_line if c.isdigit())
    CURR_PATCH = ''.join(c for c in CURRENT_PATCH if c.isdigit())
    if  CURR_PATCH != first_line:    
        write_data(DATA_FILE, CURRENT_PATCH)
    else:
        root=tk.Tk()
        root.withdraw()
        if call():
            write_data(DATA_FILE, CURRENT_PATCH)
if __name__ == "__main__":
    main()
# TODO:
#   Search on conditions(wr, champ, rank, )