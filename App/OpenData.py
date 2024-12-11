import csv
import os
from os import listdir

class fileManagment:

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) # Gives current directory
    
    def getName(self, suffix=".csv"):
        try:
            filenames = listdir(self.path) #Finds all files
            file = [filename for filename in filenames if filename.endswith(suffix)] #Loops through the file and finds csv
            return file[0] # returns the first one
        except FileNotFoundError:
            print("There was a file not found error... FileNotFoundError")
        except IndexError:
            print("There was a file not found error... IndexError")

    def openCSV(self, fileName):
        try:
            if os.path.exists(f"{self.path}/{fileName}"): #The / makes it a valid path
                with open(rf"{self.path}/{fileName}", 'r') as file:
                    data = []
                    csvFile = csv.reader(file)
                    for line in csvFile:
                        data.append(line)
                        print(line)
                        return data
            else:
                print("This file path does not exist")
        except FileNotFoundError:
            print("The file was not found")

if __name__ == '__main__':
    FM = fileManagment()
    name = FM.getName()
    FM.openCSV(name)
