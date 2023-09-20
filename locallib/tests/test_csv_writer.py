import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

sys.path.append(parent)

from unittest import main, TestCase
import logger
TestLogger = logger.setup_logging("TestLogger", False)

class test_csv(TestCase):
    def setUp(self) -> None:
        self.test_data_file_name: str = "player_data.csv"
        self.test_stats_file_name: str = "average_stats.csv"
        self.expected_columns: int = 10
        self.filenames = next(os.walk(os.path.dirname(parent)), (None, None, []))[2]
        return super().setUp()
    def test_data_file_name(self) -> None:
        self.assertTrue(self.test_data_file_name in self.filenames, "Missing player data file")

    def test_stats_file_name(self) -> None: 
        self.assertTrue(self.test_stats_file_name in self.filenames, "Missing stats data file")

    def test_data(self) -> None:
        with open('../../player_data.csv', 'r', encoding='utf-8') as file:
            first_line = file.readline()
            self.assertTrue(first_line.count(',') == self.expected_columns, f"Not matching amount of columns ({first_line.count(',')})")
    
if __name__ == "__main__":
    main()