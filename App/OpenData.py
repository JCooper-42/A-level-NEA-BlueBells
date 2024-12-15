import csv
import os
from os import listdir
import os

class fileManagment:

<<<<<<< HEAD
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
=======
    @staticmethod
    def getName(suffix=".csv"):
        try:
            path = os.getcwd()
            filenames = listdir(path) #Finds all files
            file = [filename for filename in filenames if filename.endswith(suffix)] #Loops through the file and finds csv
            return file[0] # returns the first one
        except FileNotFoundError:
            print("Is the csv in the right path?")

    @staticmethod
    def openCSV(fileName):
        values = []
        try:
            with open(rf"{os.getcwd()}\{fileName}", 'r') as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    values.append(line)
            return values
>>>>>>> a838c2bbfd289dad1815c0a676e2da302e2e902d
        except FileNotFoundError:
            print("The file was not found")

if __name__ == '__main__':
<<<<<<< HEAD
    FM = fileManagment()
=======
    FM = fileManagment
>>>>>>> a838c2bbfd289dad1815c0a676e2da302e2e902d
    name = FM.getName()
    FM.openCSV(name)
