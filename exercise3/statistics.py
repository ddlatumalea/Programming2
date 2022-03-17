# from reader import Reader

import numpy as np
import matplotlib.pyplot as plt


class AverageYear:
    # def __init__(self):
    #     self.reader = Reader()
    #
    # def get_average_temperature(self):
    #     data = self.reader.get_lines()
    #     averages = {}
    #
    #     while list(filter(None, data)):
    #
    #         for props in list(filter(None, data)):
    #             cleaned = np.array(props.rstrip().split(','), dtype=float)
    #             averages[cleaned[0]] = sum(cleaned[1:13]) / 12
    #
    #         data = self.reader.get_lines()
    #
    #     return averages

    def update(self, data):
        averages = {}

        for props in list(filter(None, data)):
            cleaned = np.array(props.rstrip().split(','), dtype=float)
            averages[cleaned[0]] = sum(cleaned[1:13]) / 12

        plt.plot(averages.keys(), averages.values(), color='blue')



class AverageMonth:
    pass


if __name__ == '__main__':
    average_year = AverageYear()
    averages = average_year.get_average_temperature()
    plt.plot(averages.keys(), averages.values())
    plt.show()


