from OpenData import fileManagment

class FunFacts(fileManagment): 

    def getData(self):
        print("Hello")
        path = fileManagment.find("C", "microbit")
        print(path)
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