import os, fnmatch
import pandas as pd

class fileManagment:

    @staticmethod
    def find(path, pattern): #Find the file on the microbit
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    def Open(self):


FM = fileManagment()
print(FM.find("D:", "MY_DATA.htm"))
