import requests
from bs4 import BeautifulSoup
import logging
import re
import logger

HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
ScrapeLogger = logger.setup_logging("ScrapeLogger", False)

class Profile_Analyzer:
    def __init__(self, link) -> None:
        self.new_webpage = requests.get(link, headers=HEADERS, timeout=60)
        self.new_soup = BeautifulSoup(self.new_webpage.content, 'lxml')
        try:
            self.leaderboard_rank:str = self.new_soup.find('span', {'class' : 'ranking'}).text.strip()
            self.leaderboard_rank = self.leaderboard_rank.replace(",", "")
            self.kda: str = self. new_soup.find('div', {'class' : 'kda'}).find_next().text.strip()
            self.ign: str = self.new_soup.find('h1', {'class' : 'summoner-name'}).text.strip()
            self.rank: str = self.new_soup.find('div', {'class' : 'tier'})
            self.lp: str = self.rank.find_next()
            self.lp = self.lp.text.strip().replace(",", "")
            self.total_games: str = self.new_soup.find('div', {'class' : 'win-lose'})
            self.winrate: str = self.total_games.find_next()
            self.winrate = self.winrate.text.strip().replace("Win Rate", "WR")
            self.most_played: str = self.new_soup.find('div', {'class' : 'champion-box'})
            self.most_played = self.most_played.find('div', {'class' : 'name'})
            self.most_played = self.most_played.find('a').text.strip()
            self.cs_min: str = self.new_soup.find('div', {'class' : 'cs'}).text.strip()
            self.cs_min = self.cs_min.replace("CS", "")
            self.cs_min = self.cs_min.replace(" ", "")
            self.cs_min = re.sub("\(.*?\)","",self.cs_min)
        except Exception:
            pass    
    def get_data(self) -> str:
        try:
            write_data: str = f"rank {self.leaderboard_rank},{self.ign},{self.rank.text.strip()},{self.lp},{self.total_games.text.strip()},{self.winrate},{self.most_played},{self.kda},{self.cs_min},\n"
        except Exception:
            ScrapeLogger.warning("Couldn't fetch information for profile rank " + self.leaderboard_rank)
            return ""
        return write_data