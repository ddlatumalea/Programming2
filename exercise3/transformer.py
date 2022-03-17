import json

class CsvConverter:

    def __init__(self):
        pass

    def csv_to_json(self, header, file):
        keys = header.rstrip().split(',')
        data_dict = []
        for line in file[1:]:
            values = line.rstrip().split(',')
            data_dict.append(dict(zip(keys, values)))

        return json.dumps(data_dict)

if __name__ == '__main__':
    with open('dSST.csv') as file:
        data = file.readlines()

    converter = CsvConverter()
    file = converter.csv_to_json(data)
    print(file)