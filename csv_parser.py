from csv import reader
from json import dumps

class CSV_Parser:
    def __init__(self, input_file):
        self.input_file = input_file
    def parse(self, encoding='UTF-8', newline='', delimiter=';'):
        with open('./viewedHistory.csv', 'r', encoding='UTF-8', newline='') as csvfile:
            r = reader(csvfile, delimiter=";")
            container = [row for row in r]
        csvfile.close()
        out = [dict(zip(container[0], i)) for i in container]
        out.pop(0)
        return dumps(out)        
