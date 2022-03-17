import linecache
import time

import matplotlib.pyplot as plt

from transformer import CsvConverter
from statistics import AverageYear


class Reader:

    def __init__(self, file_name='dSST.csv'):
        self.file = file_name
        self.converter = CsvConverter
        self.pointer = 2
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def get_lines(self):
        while True:
            lines = []
            for i in range(self.pointer, self.pointer + 5):
                lines.append(linecache.getline(self.file, i))

            if not list(filter(None, lines)):
                break

            self.pointer += 4

            print(lines)

            self.notify_observers(lines)
            lines.clear()

            plt.pause(1)
        # lines = []
        # for i in range(self.pointer, self.pointer + 5):
        #     lines.append(linecache.getline(self.file, i))
        #
        # self.pointer += 4
        #
        # return lines

    def get_header(self):
        with open(self.file) as file:
            header = file.readline()

        return header


if __name__ == '__main__':
    # observer
    reader = Reader()

    # subscriber
    year_stat = AverageYear()

    reader.add_observer(year_stat)

    reader.get_lines()
