import os, fnmatch
import csv

class fileManagment:

    @staticmethod
    def find(path, pattern): #Find the file on the microbit
        results = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    results.append(os.path.join(root, name))
                    result = results[0]
                    result = str(result)
                    return result

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
    FM.find()