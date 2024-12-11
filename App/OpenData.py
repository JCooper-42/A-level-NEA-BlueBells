import csv
from os import listdir

class fileManagment:

    @staticmethod
    def getName(path_to_dir, suffix=".csv"):
        filenames = listdir(path_to_dir) #Finds all files
        file = [filename for filename in filenames if filename.endswith(suffix)] #Loops through the file and finds csv
        return file[0] # returns the first one

    @staticmethod
    def openCSV(fileName):
        try:
            with open(rf"C:\Users\James\Documents\Computer Science A-level\Programming project\App\{fileName}", 'r') as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    print(line)
        except FileNotFoundError:
            print("The file was not found")

if __name__ == '__main__':
    print("Currently working on OpenData")
    FM = fileManagment
    name = FM.getName(r"C:\Users\James\Documents\Computer Science A-level\Programming project\App")
    FM.openCSV(name)
