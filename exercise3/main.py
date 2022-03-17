from reader import Reader
from transformer import CsvConverter
from statistics import AverageYear

if __name__ == '__main__':
    # observer
    reader = Reader()

    # subscriber
    year_stat = AverageYear()

    reader.add_observer(year_stat)

    reader.get_lines()