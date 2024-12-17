import csv
import os
from os import listdir


class fileManagment:

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) # current directory
        self.data = []
    
    def getName(self, suffix=".csv"):
        try:
            filenames = listdir(self.path) #Finds all files
            file = [filename for filename in filenames if filename.endswith(suffix)] #Loops through the file and finds csv
            return file[0] # returns the first microbit csv
        except FileNotFoundError: # exception handling
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
                        self.data.append(line)
            else:
                print("This file path does not exist")
        except FileNotFoundError:
            print("The file was not found")

    def formatData(self):
        self.data.remove(self.data[0])
        xvalues = []
        yvalues = []
        zvalues = []
        print(self.data)
        for i in range(0, len(self.data) - 1):
            xvalues.append(self.data[i][1])
            yvalues.append(self.data[i][2])
            zvalues.append(self.data[i][3])
            time = self.data[i][0]
        return xvalues, yvalues, zvalues, time

if __name__ == '__main__':
    FM = fileManagment()
    name = FM.getName()
    FM.openCSV(name)
    FM.formatData()


