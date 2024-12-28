from OpenData import fileManagment

class FunFacts(fileManagment):

    def __init__(self):
        self.xvelocity = []
        self.yvelocity =[]
        self.zvelocity = []

    def getData(self):
        FileM = fileManagment() # Make an instance of FileM in diff class
        data = FileM.getName()
        FileM.openCSV(fileName = data)
        self.xvelocity, self.yvelocity, self.zvelocity, self.time = FileM.formatData() #unpack in to instance vars

    def FunFact1(self): #Top rep speed
        return max(self.yvelocity)

if __name__ == '__main__':
    FunF = FunFacts()
    FunF.getData()
    print(FunF.FunFact1())
