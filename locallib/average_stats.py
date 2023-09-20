import pandas as pd
from typing import List
from math import floor

class Most_Frequent_Values:

    def __init__(self) -> None:
        self.data_file: str = '../player_data.csv'
        self.first_line: List[str] = self.__read_first_line()

    def __read_first_line(self) -> List[str]:
        with open(self.data_file, 'r', encoding='utf-8') as file:
            return file.readline().split(',')

    def write_data(self, patch: str) -> None:        
        df = pd.read_csv(self.data_file)
        with open('../average_stats.csv', 'w', encoding='utf-8') as file:
            file.writelines(patch + '\n')
            for i in range(2, len(self.first_line) - 3):
                file.write(f"{self.first_line[i]}:, "[1:] + str(df[self.first_line[i]].value_counts().idxmax()) + "\n")

            avg_level: float = df[self.first_line[len(self.first_line) - 3]].mean()
            avg_cs: float = df[self.first_line[len(self.first_line) - 2]].mean()

            file.write(f"{self.first_line[len(self.first_line) - 3]}:, "[1:] + str(floor(avg_level)) + "\n")
            file.write(f"{self.first_line[len(self.first_line) - 2]}:, "[1:] + str(floor(avg_cs)) + "\n")