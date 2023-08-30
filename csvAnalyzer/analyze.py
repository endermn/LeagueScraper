from typing import List
import csv

most_frequent: List[str] = []

def get_most_frequent(row_num) -> str:
    with open('../data.csv', 'r', encoding='utf-8') as file:
        most_common_list: List[str] = []
        csv_reader = csv.reader(file)
        for row in csv_reader:
            most_common_list.append(row[row_num])
        most_common_item: str = max(set(most_common_list), key=most_common_list.count)
        return most_common_item
with open('../data.csv', 'a', encoding='utf-8') as file:
    file.write('\n')
    for i in range(file.readline().count(',')):
        file.write(get_most_frequent(i))