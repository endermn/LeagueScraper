import pandas as pd
from typing import List

class Most_Frequent_Values:
    def __init__(self) -> None:
        self.data_file: str = '../player_data.csv'
        self.first_line: List[str] = self.read_first_line()

    def read_first_line(self) -> List[str]:
        with open(self.data_file, 'r', encoding='utf-8') as file:
            return file.readline().split(',')

    def write_data(self, patch: str) -> None:        
        df = pd.read_csv(self.data_file)
        with open('../average_stats.csv', 'w', encoding='utf-8') as file:
            file.writelines(patch + '\n')
            for i in range(2, len(self.first_line) - 2):
                file.write(f"{self.first_line[i]}:, " + df[self.first_line[i]].value_counts().idxmax() + "\n")
            file.write(f"{self.first_line[len(self.first_line) - 2]}:, " + str(df[self.first_line[len(self.first_line) - 2]].mean()))
if __name__ == "__main__":
    Most_Frequent_Values().write_data()