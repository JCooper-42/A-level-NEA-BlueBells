import os, fnmatch
from bs4 import BeautifulSoup

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

    def OpenHTM(self, pathToFile):
        with open(pathToFile, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
        tables = soup.find_all('table')
        print(tables)


FM = fileManagment()
path = FM.find("D:", "MY_DATA.htm")
print(path)
FM.OpenHTM(path)
