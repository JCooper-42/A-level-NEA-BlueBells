import csv
from os import listdir

class fileManagment:

    @staticmethod
    def find(path_to_dir, suffix=".csv"):
        filenames = listdir(path_to_dir)
        return [filename for filename in filenames if filename.endswith(suffix)]

    @staticmethod
    def openCSV(path):
        try:
            with open(path, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    print(row)
        except FileNotFoundError:
            print("The file was not found")

if __name__ == '__main__':
    FM = fileManagment
    print(FM.find(r"C:\Users\James\Documents\Computer Science A-level\Programming project\App"))