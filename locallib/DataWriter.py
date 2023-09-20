from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
import tkinter as tk

from typing import List

from ProfileAnalyzer import Profile_Analyzer
import ProfileScraper
import FileManager
import average_stats
import PatchScraper


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
        FileManager.clear_file(DATA_FILE)
        with open(DATA_FILE, 'a', encoding="utf-8") as file:
            file.write('Rank, IGN, Tier, LP, Win-Lose, Winrate, Most Played, KDA, Avg Level, Avg CS, \n')

            for i in range(1, PAGES + 1):
                url: str = f"https://www.op.gg/leaderboards/tier?region=euw&page={i}"

                try:
                    resp = requests.get(url, headers=HEADERS, timeout=60)
                except requests.exceptions.ConnectionError:
                    pass
                soup = BeautifulSoup(resp.content, "lxml")
                profiles: List[str] = ProfileScraper.Scraper(soup).scrape_profiles()
                
                for i in range(10):
                    Analyzer = Profile_Analyzer(self.stat_site_url + profiles[i])
                    file.write(Analyzer.get_data())
        
        average_stats.Most_Frequent_Values().write_data(patch)

    def check_patch_value(self) -> None:
        CURRENT_PATCH = PatchScraper.scrape_patch(self.patch_url, HEADERS)
        
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
