from OpenData import fileManagment

class FunFacts(fileManagment): 

    @staticmethod
    def getData():
        Data = fileManagment.openCSV(fileName = fileManagment.getName())
        print(Data)

    def formatData(self):
        pass

    def calcDisplament(self):
        pass

    def FunFact1(self):
        pass

if __name__ == '__main__':
    FF = FunFacts()
