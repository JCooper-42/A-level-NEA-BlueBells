import csv
from os import listdir
import os

class fileManagment:

    @staticmethod
    def getName(suffix=".csv"):
        path = os.getcwd()
        filenames = listdir(path) #Finds all files
        file = [filename for filename in filenames if filename.endswith(suffix)] #Loops through the file and finds csv
        return file[0] # returns the first one

    @staticmethod
    def openCSV(fileName):
        try:
            with open(rf"{os.getcwd()}\{fileName}", 'r') as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    print(line)
        except FileNotFoundError:
            print("The file was not found")

if __name__ == '__main__':
    FM = fileManagment
    name = FM.getName()
    FM.openCSV(name)
