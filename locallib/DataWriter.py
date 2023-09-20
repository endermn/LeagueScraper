from bs4 import BeautifulSoup
import requests
from typing import List
from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager
import most_frequent
import PatchScraper
import tkinter as tk
from tkinter import messagebox


DATA_FILE: str = "../player_data.csv"
PAGES: int = 1
HEADERS: dict[str, str] = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

class DataWriter():
    def __init__(self) -> None:
        self.patch_url = "https://www.leagueoflegends.com/en-us/news/tags/patch-notes/"
        self.stat_site_url = "https://op.gg"

    def __msgbox(self) -> bool:
        return messagebox.askquestion('Refresh data', 'Do you really want to refresh the data') == "yes"

    def __write_data(self, patch: str) -> None:
        FileManager.Manager(DATA_FILE).clear_file()
        with open(DATA_FILE, 'a', encoding="utf-8") as file:
            file.write('Rank, IGN, Tier, LP, Win-Lose, Winrate, Most Played, KDA, Avg CS, KP, \n')

            for i in range(1, PAGES + 1):
                url: str = f"https://www.op.gg/leaderboards/tier?region=euw&page={i}"

                try:
                    resp = requests.get(url, headers=HEADERS, timeout=60)
                except requests.exceptions.ConnectionError:
                    pass
                soup = BeautifulSoup(resp.content, "lxml")
                profiles: List[str] = ProfileScraper.Scraper(soup).scrape_profiles()
                
                for profile in range(5):
                    Analyzer = Profile_Analyzer(self.stat_site_url + profiles[profile])
                    file.write(Analyzer.get_data())
        
        most_frequent.Most_Frequent_Values().write_data(patch)

    def check_patch_value(self) -> None:
        Patch = PatchScraper.Patch(self.patch_url, HEADERS)
        CURRENT_PATCH = Patch.scrape_patch()
        first_line: str = ""
        
        with open('../average_stats.csv', 'r', encoding='utf-8') as file:
            first_line = file.readline()

        first_line = ''.join(c for c in first_line if c.isdigit())
        CURR_PATCH = ''.join(c for c in CURRENT_PATCH if c.isdigit())
        
        if  CURR_PATCH != first_line:    
            self.__write_data(CURRENT_PATCH)
        else:
            root=tk.Tk()
            root.withdraw()
            if self.__msgbox():
                self.__write_data(CURRENT_PATCH)
            else:
                exit(1)
