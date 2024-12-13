from OpenData import fileManagment

class FunFacts(fileManagment): 

    @staticmethod
    def getData():
        path = fileManagment.getName("C", "microbit")
        fileManagment.openCSV(path)

    def formatData(self):
        pass

    def calcDisplament(self):
        pass

    def FunFact1(self):
        pass

if __name__ == '__main__':
    FF = FunFacts()
    print(FF.getData())