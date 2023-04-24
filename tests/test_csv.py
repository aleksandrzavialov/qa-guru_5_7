import csv
import os
from conftest import PROJECT_RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv_processing():
    csv_path_to_file = os.path.join(PROJECT_RESOURCE_PATH, 'eggs.csv')
    with open(csv_path_to_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path_to_file) as csvfile:
        csvreader = csv.reader(csvfile)
        assert csv.reader.__sizeof__() == 56
        for row in csvreader:
            assert len(row) == 3
            print(row)
