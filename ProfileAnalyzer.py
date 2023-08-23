import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

class Profile_Analyzer:
    def __init__(self, link) -> None:
        self.new_webpage = requests.get(link, headers=HEADERS, timeout=60)
        self.new_soup = BeautifulSoup(self.new_webpage.content, 'lxml')
        self.leaderboard_rank = self.new_soup.find('div', {'class' : 'ladder-ranking'})
        self.leaderboard_rank = self.leaderboard_rank.find('span').find('strong').text.strip()
        self.kda =self. new_soup.find('div', {'class' : 'champion-stats_col champion-stats_col-2'})
        self.kda = self.kda.find('span').text.strip()
        self.ign = self.new_soup.find('div', {'class' : 'summoner-name'}).find('span').text.strip()
        self.rank = self.new_soup.find('span', {'class' : 'rank-title'})
        self.lp = self.rank.find_next()
        self.lp = self.lp.text.strip().replace(",", "")
        self.total_games = self.new_soup.find('span', {'class' : 'total-games'})
        self.winrate = self.total_games.find_next()
        self.winrate = self.winrate.text.strip().replace("Win Rate", "WR")
        self.most_played = self.new_soup.find('div', {'class' : 'champion-name'}).text.strip()
    def get_data(self) -> str:
        write_data = f"rank {self.leaderboard_rank},{self.ign},{self.rank.text.strip()},{self.lp},{self.total_games.text.strip()},{self.winrate},{self.most_played},{self.kda} KDA, \n"
        print(write_data)
        return write_data