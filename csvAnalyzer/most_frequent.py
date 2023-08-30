import pandas as pd
from typing import List

class Most_Frequent_Values:
    def __init__(self) -> None:
        self.data_file = '../player_data.csv'
        self.first_line = self.__read_first_line()
        
    def __read_first_line(self) -> List[str]:
        with open(self.data_file, 'r', encoding='utf-8') as file:
            return file.readline().split(',')
    def write_data(self) -> None:        
        df = pd.read_csv(self.data_file)
        with open('../average_stats.csv', 'w', encoding='utf-8') as file:
            for i in range(2, len(self.first_line) - 2):
                file.write(f"{self.first_line[i]}:, " + df[self.first_line[i]].value_counts().idxmax() + "\n")

if __name__ == "__main__":
    Most_Frequent_Values().write_data()